# Draw a Number Neural Network

This is a simple neural network application that allows users to draw digits (0-9) on a 5x5 grid and predict the digit using a trained neural network. The application is built using Python's Tkinter library for the GUI and NumPy for numerical computations.

## Features

- Draw digits on a 5x5 canvas.
- Predict the drawn digit using a neural network.
- Train the neural network with user-defined labels for continuous learning.
- Clear the canvas for new drawings.

## Requirements

To run this application, you need to have Python 3 installed along with the following packages:

- `numpy`
- `tkinter` (usually comes pre-installed with Python)

You can install NumPy using pip if you haven't already:

```bash
pip install numpy
```

## Usage

1. **Run the Application**: Execute the script to start the application.

    ```bash
    python draw_number.py
    ```

2. **Drawing**: Use the mouse to draw a digit on the canvas. Click and drag to fill in the grid.

3. **Label Input**: Enter the correct label (0-9) for the drawn digit in the entry box.

4. **Training**: Click the "Train" button to train the neural network with the drawn digit and its corresponding label.

5. **Prediction**: Click the "Predict" button to let the neural network predict the drawn digit based on its current training.

6. **Clear Canvas**: Use the "Clear" button to reset the canvas for a new drawing.

## Code Overview

- **NeuralNetwork Class**: Implements a basic feedforward neural network with one hidden layer.
    - Methods:
        - `forward(x)`: Performs a forward pass and returns the network's output.
        - `train(x, y, learning_rate, epochs)`: Trains the network using backpropagation.
  
- **DrawApp Class**: Manages the Tkinter GUI and handles user interactions.
    - Methods:
        - `paint(event)`: Handles drawing on the canvas.
        - `clear()`: Clears the canvas.
        - `predict()`: Predicts the digit using the current neural network weights.
        - `train()`: Trains the network with the provided label.

## Example Patterns and Results

Below are the 5x5 patterns used to train the model. Each row shows the digit, the grid pattern representing it, and the model's expected prediction.

### 5x5 Patterns for Digits (0-9)

| Digit | Pattern | Model Prediction |
|-------|---------|------------------|
| **0** | ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) | **0** |
| **1** | ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+)<br>![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+)<br>![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+)<br>![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+)<br>![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) | **1** |
| **2** | ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+) ![ ](https://via.placeholder.com/15/ffffff/ffffff?text=+)<br>![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) ![0](https://via.placeholder.com/15/000000/000000?text=+) | **2** |
| **3** | Similar to **2** pattern with slight differences. | **3** |
| **4** | Vertical and horizontal patterns to match **4** structure. | **4** |
| **5** | Horizontal top and bottom, vertical middle. | **5** |
| **6** | Closed loop pattern similar to **0** but with middle. | **6** |
| **7** | Horizontal top, descending diagonal. | **7** |
| **8** | Full closed loop like two **0s**. | **8** |
| **9** | **0** pattern with right upper side. | **9** |

## Data fragmentation

For optimal performance, it's crucial to ensure that data fragmentation is less than 50%. Data fragmentation refers to a situation where the training data does not adequately represent the diversity of input patterns that the model may encounter. When the model is trained on a fragmented dataset, it may learn biases or fail to generalize well, leading to inaccurate predictions.

### Understanding Data Fragmentation

Data fragmentation can occur in various forms:

1. **Underrepresentation of Classes**: If certain digits are drawn much less frequently than others in the training set, the model may struggle to accurately recognize those digits.

2. **Insufficient Variety in Drawings**: If the same patterns of digits are repeated without variation, the model may not learn to recognize different ways the same digit can be represented.

3. **Lack of Noise or Distortions**: In real-world scenarios, digits might be drawn with variations such as different sizes, rotations, or noise. If the training set lacks such diversity, the model may fail to recognize distorted inputs.

## Notes

- The neural network is initialized with random weights and requires training to improve its accuracy.
- The training epochs can be adjusted to fine-tune the learning process.
- The model's performance may vary based on the training data and the complexity of the drawings.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- This project utilizes the NumPy library for efficient numerical calculations.
- Tkinter is used for creating the graphical user interface.

### Instructions for Use:
- Save this content in a file named `README.md` in the same directory as your Python script.
- Adjust any sections as needed to better fit your project's specifics or any additional features you may want to highlight.
