### Single-Layer Perceptrons
A single-layer perceptron is a fundamental building block of neural networks, used for binary classification of linearly separable data. It consists of an input layer, weights, a bias, and an activation function to produce a binary output (0 or 1). While TensorFlow simplifies implementation, the perceptron's core concepts apply across all programming environments.

* **Input Layer:** Takes a vector of input features (e.g., a 2D input for two features).
* **Weights:** Each input is multiplied by a weight, determining its influence on the output.
* **Bias:** A constant added to the weighted sum, adjusting the decision boundary.
* **Activation Function:** Typically a step function (in classic perceptrons) or sigmoid (in modern implementations), mapping the weighted sum to a binary output.
* **Training Process:** Adjusts weights and bias to minimize prediction errors using a learning algorithm (e.g., gradient descent or the perceptron learning rule).
* **Limitations:** Can only solve linearly separable problems (e.g., AND, OR, but not XOR).
* **General Implementation:** Requires manual computation of weighted sums, activation, and weight updates using loops and basic math operations in languages like Python, C, or Java.

### Creating a Single-Layer Perceptron with TensorFlow

TensorFlow's Keras API simplifies perceptron implementation by abstracting low-level math. You define a model with a Dense layer, specify an optimizer and loss function, and train it on data. TensorFlow handles backpropagation and optimization, making it efficient for rapid prototyping and scalable applications.

Example:
```python
import tensorflow as tf
import numpy as np

# Sample data (AND operation)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [0], [0], [1]])

# Define perceptron
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[2], activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy')

# Train
model.fit(X, y, epochs=1000, verbose=0)

# Predict
predictions = model.predict(X)
print("Predictions (rounded):")
print(predictions.round())
```

Output:
```commandline
Predictions (rounded):
[[0.]
 [0.]
 [0.]
 [1.]]
```

### Challenge Instructions
Follow these steps to complete this challenge!
1. Create a new Python file in your home directory (e.g., perceptron.py).
2. Import the required libraries: tensorflow as tf and numpy as np.
3. Define a dataset with the following:
    * Input `X`: A 4x2 NumPy array `[[0, 0], [0, 1], [1, 0], [1, 1]]` representing input pairs.
    * Output `y`: A 4x1 NumPy array `[[0], [0], [0], [1]]` representing AND-like labels (1 only when both inputs are 1).
4. Build a single-layer perceptron using `tf.keras.Sequential` with:
    * One `Dense` layer with 1 unit
    * Input shape of `2`
    * `sigmoid` activation to output values between 0 and 1
5. Compile the model with:
    * `adam` optimizer for efficient gradient descent.
    * `binary_crossentropy` loss function, suitable for binary classification.
6. Train the model on X and y for 1000 epochs with verbose=0 to suppress training output.
7. Use the trained model to predict outputs for X, rounding predictions to 0 or 1 using .round().
8. Print the rounded predictions with a header **"Predictions (rounded):"** in the format shown below.
9. Save your program and run it to test the output.
10. To get the flag, run `/challenge/verify <yourfile>.py` to verify your solution.

Example output:
```commandline
Predictions (rounded):
[[0.]
 [0.]
 [0.]
 [1.]]
```