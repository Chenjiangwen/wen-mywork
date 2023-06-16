'''
####################### Q1 f. #########################
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler


def ridge_regression_loss(X, y, beta, phi):
    n = X.shape[0]
    return (1 / n) * np.sum((y - X.dot(beta)) ** 2) + phi * np.sum(beta ** 2)


def ridge_regression_gradient(X, y, beta, phi):
    n = X.shape[0]
    return (-2 / n) * X.T.dot(y - X.dot(beta)) + 2 * phi * beta


def batch_gradient_descent(X, y, beta_init, step_size, epochs, phi):
    beta = beta_init
    loss_history = []
    for _ in range(epochs):
        beta -= step_size * ridge_regression_gradient(X, y, beta, phi)
        loss_history.append(ridge_regression_loss(X, y, beta, phi))
    return beta, loss_history


def train_test_MSE(beta, X_train, y_train, X_test, y_test):
    train_mse = (1 / X_train.shape[0]) * np.sum((y_train - X_train.dot(beta)) ** 2)
    test_mse = (1 / X_test.shape[0]) * np.sum((y_test - X_test.dot(beta)) ** 2)
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
Y_train = data_scaled.iloc[:n//2, 0]
Y_test = data_scaled.iloc[n//2:, 0]

phi = 0.5
epochs = 1000
step_sizes = [0.000001, 0.000005, 0.00001, 0.00005, 0.0001, 0.0005, 0.001, 0.005, 0.01]
beta_init = np.ones(X_train.shape[1])

# Calculate the closed form ridge solution
beta_closed_form = np.linalg.inv(X_train.T.dot(X_train) + phi * np.eye(X_train.shape[1])).dot(X_train.T).dot(Y_train)

fig, axes = plt.subplots(3, 3, figsize=(15, 15))
axes = axes.ravel()

best_beta = None
best_step_size = None
lowest_test_mse = float('inf')

for i, step_size in enumerate(step_sizes):
    beta_gd, loss_history = batch_gradient_descent(X_train, Y_train, beta_init, step_size, epochs, phi)
    delta = np.array(loss_history) - ridge_regression_loss(X_train, Y_train, beta_closed_form, phi)


    train_mse, test_mse = train_test_MSE(beta_gd, X_train, Y_train, X_test, Y_test)
    if test_mse < lowest_test_mse:
        best_beta = beta_gd
        best_step_size = step_size
        lowest_test_mse = test_mse

    ax = axes[i]
    ax.plot(delta)
    ax.set_title(f"Step size: {step_size}")
    ax.set_xlabel("Epochs")
    ax.set_ylabel("Delta")

plt.tight_layout()
plt.savefig('f_plot.png')
plt.show()

train_mse, test_mse = train_test_MSE(best_beta, X_train, Y_train, X_test, Y_test)
print(f"Best step size: {best_step_size}")
print(f"Train MSE: {train_mse}")
print(f"Test MSE: {test_mse}")