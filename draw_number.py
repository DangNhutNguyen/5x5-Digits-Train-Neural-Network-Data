import tkinter as tk
import numpy as np

# Sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network class
class NeuralNetwork:
    def __init__(self):
        self.input_size = 25  # 5x5 input grid
        self.hidden_size = 16
        self.output_size = 10  # 0-9 digits

        # Randomly initialize weights
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)

    def forward(self, x):
        self.hidden = sigmoid(np.dot(x, self.weights_input_hidden))
        self.output = sigmoid(np.dot(self.hidden, self.weights_hidden_output))
        return self.output

    def train(self, x, y, learning_rate=0.1, epochs=10000):
        for _ in range(epochs):
            # Forward pass
            hidden_layer_input = np.dot(x, self.weights_input_hidden)
            hidden_layer_output = sigmoid(hidden_layer_input)
            final_layer_input = np.dot(hidden_layer_output, self.weights_hidden_output)
            final_layer_output = sigmoid(final_layer_input)

            # Backpropagation
            output_error = y - final_layer_output
            output_delta = output_error * sigmoid_derivative(final_layer_output)

            hidden_error = output_delta.dot(self.weights_hidden_output.T)
            hidden_delta = hidden_error * sigmoid_derivative(hidden_layer_output)

            # Update weights
            self.weights_hidden_output += hidden_layer_output.T.dot(output_delta) * learning_rate
            self.weights_input_hidden += x.T.dot(hidden_delta) * learning_rate

class DrawApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Draw a Number")
        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()
        self.canvas.bind("<B1-Motion>", self.paint)
        self.grid = [[0] * 5 for _ in range(5)]
        self.cell_size = 40
        
        # Initialize Neural Network
        self.nn = NeuralNetwork()
        
        # Prediction and Training button
        self.predict_button = tk.Button(master, text="Predict", command=self.predict)
        self.predict_button.pack()
        
        # Label input for training
        self.label_entry = tk.Entry(master)
        self.label_entry.pack()
        self.label_entry.insert(0, "Enter label (0-9)")
        
        # Train button
        self.train_button = tk.Button(master, text="Train", command=self.train)
        self.train_button.pack()

    def paint(self, event):
        x, y = event.x // self.cell_size, event.y // self.cell_size
        if 0 <= x < 5 and 0 <= y < 5:
            self.grid[y][x] = 1
            self.canvas.create_rectangle(
                x * self.cell_size, y * self.cell_size,
                (x + 1) * self.cell_size, (y + 1) * self.cell_size, fill="black"
            )

    def clear(self):
        self.grid = [[0] * 5 for _ in range(5)]
        self.canvas.delete("all")

    def predict(self):
        x = np.array(self.grid).flatten().reshape(1, 25)  # Flattened 5x5 grid
        prediction = self.nn.forward(x)
        predicted_number = np.argmax(prediction)
        print("Predicted number:", predicted_number)
        
        # Display predicted number in a label
        self.result_label.config(text=f"Predicted: {predicted_number}")

    def train(self):
        label = self.label_entry.get()
        if label.isdigit() and 0 <= int(label) < 10:
            # Convert label to one-hot encoded vector
            y = np.zeros((1, 10))
            y[0][int(label)] = 1
            
            x = np.array(self.grid).flatten().reshape(1, 25)  # Flattened 5x5 grid
            self.nn.train(x, y, learning_rate=0.1, epochs=100)  # Train for a few epochs
            print(f"Trained with label: {label}")
        else:
            print("Please enter a valid label (0-9).")

root = tk.Tk()
app = DrawApp(root)
clear_button = tk.Button(root, text="Clear", command=app.clear)
clear_button.pack()

# Result label for displaying predictions
app.result_label = tk.Label(root, text="")
app.result_label.pack()

root.mainloop()
