'''
####################### Q1 j. #########################
'''
import numpy as np
import pandas as pd
from keras.losses import mean_squared_error
from matplotlib import pyplot as plt
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
    n = X.shape[0]
    for _ in range(epochs):
        for i in range(n):
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
y_train = data_scaled.iloc[:n//2, 0]
y_test = data_scaled.iloc[n//2:, 0]

phi = 0.5
epochs = 5
step_sizes_bgd = [1 / (2 * n * phi)]
beta_init = np.ones(X_train.shape[1])

# Calculate the closed form ridge solution
beta_closed_form = np.linalg.inv(X_train.T.dot(X_train) + phi * np.eye(X_train.shape[1])).dot(X_train.T).dot(y_train)


best_beta = None
best_step_size = None
lowest_test_mse = float('inf')

k_bgd = []
loss_history_bgd = []
for i, step_size in enumerate(step_sizes_bgd):
    beta_gd, loss_history_bgd = batch_gradient_descent(X_train, y_train, beta_init, step_size, epochs, phi)
    delta = np.array(loss_history_bgd) - ridge_regression_loss(X_train, y_train, beta_closed_form, phi)

    train_mse, test_mse = train_test_MSE(beta_gd, X_train, y_train, X_test, y_test)
    if test_mse < lowest_test_mse:
        best_beta = beta_gd
        best_step_size = step_size
        lowest_test_mse = test_mse

k_bgd = np.arange(len(loss_history_bgd))
delta_bgd = loss_history_bgd - loss_history_bgd[-1]
train_mse, test_mse = train_test_MSE(best_beta, X_train, y_train, X_test, y_test)


#####################

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


# 定义坐标梯度下降算法函数
def coordinate_gradient_descent(X, y, beta_init, phi, num_cycles):
    p = X.shape[1]
    beta = beta_init
    loss_history_cgd = []  # 保存每次迭代的损失函数值
    for _ in range(num_cycles):
        for j in range(p):
            beta_j = beta[j]   # 保存原来的 beta 值
            # 计算在这一维的梯度下降
            grad = -2 * X.iloc[:, j].T @ (y - X @ beta) / n + 2 * phi * beta[j]
            beta[j] -= phi * grad   # 更新 beta 值
            # 计算新的损失函数值并保存到列表中
            loss = ridge_regression_loss(X, y, beta, phi)
            loss_history_cgd.append(loss)
    return beta, loss_history_cgd

# Load train and test data here
data = pd.read_csv('CarSeats.csv')
data = data.drop(columns=['ShelveLoc', 'Urban', 'US'])


step_sizes_sgd = [1 / (2 * n * phi)]
beta_init = np.ones(X_train.shape[1])

best_beta = None
best_step_size = None
lowest_test_mse = float('inf')

k_sgd = []
loss_history_sgd = []
for i, step_size in enumerate(step_sizes_sgd):
    beta_sgd, loss_history_sgd = sgd(X_train, y_train, beta_init, step_size, epochs, phi)

    train_mse, test_mse = train_test_MSE(beta_sgd, X_train, y_train, X_test, y_test)
    if test_mse < lowest_test_mse:
        best_beta = beta_sgd
        best_step_size = step_size
        lowest_test_mse = test_mse

k_sgd = np.arange(len(loss_history_sgd))
delta_sgd = loss_history_sgd - loss_history_sgd[-1]
train_mse, test_mse = train_test_MSE(best_beta, X_train, y_train, X_test, y_test)

##########################
# 坐标梯度下降
beta_cgd, loss_history_cgd = coordinate_gradient_descent(X_train, y_train, beta_init, phi, num_cycles=10)
y_train_pred_cgd = X_train @ beta_cgd
y_test_pred_cgd = X_test @ beta_cgd
mse_train_cgd = mean_squared_error(y_train, y_train_pred_cgd)
mse_test_cgd = mean_squared_error(y_test, y_test_pred_cgd)


# 绘制进度图
k_bgd = np.arange(len(loss_history_bgd))
k_sgd = np.arange(len(loss_history_sgd))
k_cgd = np.repeat(np.arange(X_train.shape[1]), len(loss_history_cgd)//X_train.shape[1])

delta_bgd = loss_history_bgd - loss_history_bgd[-1]
delta_sgd = loss_history_sgd - loss_history_sgd[-1]
delta_cgd = loss_history_cgd - loss_history_cgd[-1]

plt.figure(figsize=(10, 6))
plt.plot(k_bgd, delta_bgd, label=f'BGD', color='g')
plt.plot(k_sgd, delta_sgd, label=f'SGD', color='b')
plt.plot(k_cgd, delta_cgd, label=f'CGD', color='r')

plt.xlabel('Number of Updates')
plt.ylabel('Delta Loss')
plt.title('Progression of Gradient Descent Algorithms')
plt.legend()
plt.savefig('j_plot.png')
plt.show()

print(f'Train MSE (CGD): {mse_train_cgd:.4f}')
print(f'Test MSE (CGD): {mse_test_cgd:.4f}')
