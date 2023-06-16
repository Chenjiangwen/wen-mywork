'''
####################### Q1 a. #########################
'''
import numpy as np


def gradient_descent(A, b, x0, alpha, gamma, tolerance):
    x = x0
    x_values = [x0]
    k = 0
    while True:
        gradient = A.T @ (A @ x - b) + gamma * x
        x = x - alpha * gradient
        x_values.append(x)
        k += 1
        if np.linalg.norm(gradient) < tolerance:
            break
    return x_values

A = np.array([[1, 2, 1, -1], [-1, 1, 0, 2], [0, -1, -2, 1]])
b = np.array([3, 2, -2])
x0 = np.array([1, 1, 1, 1])
alpha = 0.1
gamma = 0.2
tolerance = 0.001

x_values = gradient_descent(A, b, x0, alpha, gamma, tolerance)

# Print first 5 and last 5 values
for k in range(5):
    print(f"k = {k}, x^{(k)} = {x_values[k].round(4)}")

print("...")

for k in range(-5, 0):
    print(f"k = {len(x_values) + k}, x^{(k)} = {x_values[k].round(4)}")