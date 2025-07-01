import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
#linear regression

# Training data (x and y)
x = tf.constant([1.0, 2.0, 3.0, 4.0])
y_true = tf.constant([3.0, 5.0, 7.0, 9.0])  # y = 2x + 1

# Variables for weight and bias
W = tf.Variable(0.0)
b = tf.Variable(0.0)

learning_rate = 0.01

for epoch in range(10000):
    with tf.GradientTape() as tape:
        y_pred = W * x + b
        loss = tf.reduce_mean(tf.square(y_true - y_pred))  # MSE loss
    
    # Calculate gradients of loss w.r.t W and b
    gradients = tape.gradient(loss, [W, b])
    
    # Update W and b
    W.assign_sub(learning_rate * gradients[0])
    b.assign_sub(learning_rate * gradients[1])

print(f"Trained W: {W.numpy()}, b: {b.numpy()}")