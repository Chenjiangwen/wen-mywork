'''
####################### Q1 g. #########################
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler


def ridge_regression_loss(X, y, beta, phi):
    n = X.shape[0]
    return (1 / n) * np.sum((y - X.dot(beta)) ** 2) + phi * np.sum(beta ** 2)


def ridge_regression_gradient(x_i, y_i, beta, phi):
    return (-2) * x_i.T.dot(y_i - x_i.dot(beta)) + 2 * phi * beta


def sgd(X, y, beta_init, step_size, epochs, phi):
    beta = beta_init.copy()
    loss_history = []
    n = X.shape[0]
    for _ in range(epochs):
        for i in range(n):
            x_i = X.iloc[i].values.reshape(1, -1)

            y_i = y[i]
            beta -= step_size * ridge_regression_gradient(x_i, y_i, beta, phi)
            loss_history.append(ridge_regression_loss(X, y, beta, phi))
    return beta, loss_history


def train_test_MSE(beta, X_train, y_train, X_test, y_test):
    train_mse = (1 / X_train.shape[0]) * np.sum((y_train - X_train.dot(beta)) ** 2 - np.mean(y_train - X_train.dot(beta)))
    test_mse = (1 / X_test.shape[0]) * np.sum((y_test - X_test.dot(beta)) ** 2 - np.mean(y_test - X_test.dot(beta)))
    return train_mse, test_mse


# Load train and test data here
data = pd.read_csv('CarSeats.csv')
data = data.drop(columns=['ShelveLoc', 'Urban', 'US'])

scaler = StandardScaler()
data_scaled = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

data_scaled['Sales'] = data_scaled['Sales'] - data_scaled['Sales'].mean()
n = len(data_scaled)
X_train = data_scaled.iloc[:n//2, 1:]
X_test = data_scaled.iloc[n//2:, 1:]
y_train = data_scaled.iloc[:n//2, 0]
y_test = data_scaled.iloc[n//2:, 0]

phi = 0.5
epochs = 5
step_sizes = [0.000001, 0.000005, 0.00001, 0.00005, 0.0001, 0.0005, 0.001, 0.006, 0.02]
beta_init = np.ones(X_train.shape[1])

fig, axes = plt.subplots(3, 3, figsize=(15, 15))
axes = axes.ravel()

best_beta = None
best_step_size = None
lowest_test_mse = float('inf')

for i, step_size in enumerate(step_sizes):
    beta_sgd, loss_history = sgd(X_train, y_train, beta_init, step_size, epochs, phi)

    train_mse, test_mse = train_test_MSE(beta_sgd, X_train, y_train, X_test, y_test)
    if test_mse < lowest_test_mse:
        best_beta = beta_sgd
        best_step_size = step_size
        lowest_test_mse = test_mse

    ax = axes[i]
    ax.plot(loss_history)
    ax.set_title(f"Step size: {step_size}")
    ax.set_xlabel("Iterations")
    ax.set_ylabel("Loss")

plt.tight_layout()
plt.savefig('g_plot.png')
plt.show()

train_mse, test_mse = train_test_MSE(best_beta, X_train, y_train, X_test, y_test)
print(f"Best step size: {best_step_size}")
print(f"Train MSE: {train_mse}")
print(f"Test MSE: {test_mse}")