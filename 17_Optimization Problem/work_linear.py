import numpy as np
from scipy.optimize import linprog
import numpy as np
def interior_point_method(A, b, c, x, ite=1000, delta=0.001):
    m, n = A.shape
    D = x * np.eye(n, n)
    res = np.diag(D)
    for i in range(ite):
        res = np.diag(D).copy()
        t = A.dot(D)
        p = np.eye(D.shape[1]) - t.T.dot(np.linalg.inv(np.matmul(t, t.T))).dot(t)
        D += (D.dot(p).dot(D).dot(c.T)) / np.linalg.norm(p.dot(D).dot(c.T))
        D = np.diag(D) * (np.eye(n, n))
        resnew = np.diag(D)
        if (sum(abs(resnew - res))) < delta:
            break
    return np.round(res, decimals=3)



# 第一个用例
A1 = np.matrix([[-1, -1]])
b1 = np.matrix([[-3]])
c1 = np.matrix([-6, -3])
x01 = np.array([1, 0])
tol1 = 0.001

# 第二个用例：
A2 = np.matrix([[-1, -1]])
b2 = np.matrix([[-2]])
c2 = np.matrix([-2, 0])
x02 = np.array([3, 0])
tol2 = 0.001

# 第三个用例：
A3 = np.matrix([[-1, -1]])
b3 = np.matrix([[-1]])
c3 = np.matrix([0, 0])
x03 = np.array([1, 0])
tol3 = 0.001

# 第四个用例：
A4 = np.matrix([[1, 2]])
b4 = np.matrix([[4]])
c4 = np.matrix([-4, -4])
x04 = np.array([1, 0])
tol4 = 0.001


# 第五个用例：
A5 = np.matrix([[-1, -1], [1, -2]])
b5 = np.matrix([[-100], [0]])
c5 = np.matrix([-98, -277])
x05 = np.array([0, 1])
tol5 = 0.001

# result5 = interior_point_method(A5, b5, c5, x05)
# if result5 is not None:
#     print("第五个用例的最优解:", result5)
