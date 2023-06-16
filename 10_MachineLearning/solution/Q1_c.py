'''
####################### Q1 c. #########################
'''
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('CarSeats.csv')
data = data.drop(columns=['ShelveLoc', 'Urban', 'US'])

scaler = StandardScaler()
data_scaled = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

print("Mean of standardized features:\n", data_scaled.mean())
print("Variance of standardized features:\n", data_scaled.var())
data_scaled['Sales'] = data_scaled['Sales'] - data_scaled['Sales'].mean()
n = len(data_scaled)
X_train = data_scaled.iloc[:n//2, 1:]
X_test = data_scaled.iloc[n//2:, 1:]
Y_train = data_scaled.iloc[:n//2, 0]
Y_test = data_scaled.iloc[n//2:, 0]

print("First row of X_train:\n", X_train.iloc[0])
print("Last row of X_train:\n", X_train.iloc[-1])
print("First row of X_test:\n", X_test.iloc[0])
print("Last row of X_test:\n", X_test.iloc[-1])
print("First and last values of Y_train:\n", Y_train.iloc[0], Y_train.iloc[-1])
print("First and last values of Y_test:\n", Y_test.iloc[0], Y_test.iloc[-1])

'''
####################### Q1 d. #########################
'''
phi = 0.5
X_train_T = X_train.T
I = np.eye(X_train.shape[1])

beta_ridge = np.linalg.inv(X_train_T.dot(X_train) + phi * I).dot(X_train_T).dot(Y_train)
print("Ridge solution for the training dataset with φ = 0.5:\n", beta_ridge)
