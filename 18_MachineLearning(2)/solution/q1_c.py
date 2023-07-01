from sklearn.ensemble import GradientBoostingRegressor
import numpy as np
import matplotlib.pyplot as plt

# true function
def f(x):
    t1 = np.sqrt(x * (1-x))
    t2 = (2.1 * np.pi) / (x + 0.05)
    t3 = np.sin(t2)
    return t1*t3

# def f_sampler(f, n=100, sigma=0.05):
def f_sampler(f, n=100, sigma=0.05, alpha=0.1):  # 添加 alpha 参数
    # sample points from function f with Gaussian noise (0,sigma**2)
    xvals = np.random.uniform(low=0, high=1, size=n)
    # yvals = f(xvals) + sigma * np.random.normal(0,1,size=n)
    yvals = f(xvals) + sigma * np.random.normal(0,1,size=n) + alpha  # 添加 alpha 步长

    return xvals, yvals

np.random.seed(123)
# X, y = f_sampler(f, 160, sigma=0.2)
X, y = f_sampler(f, 160, sigma=0.2, alpha=0.1)  # 添加 alpha 参数
X = X.reshape(-1,1)

fig, axes = plt.subplots(5, 2, figsize=(12, 20))

base_learners = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

for i, ax in enumerate(axes.flatten()):
    n_learners = base_learners[i]
    gbr = GradientBoostingRegressor(n_estimators=n_learners).fit(X,y)
    xx = np.linspace(0,1,1000)
    ax.plot(xx, f(xx), alpha=0.5, color='red', label='truth')
    ax.scatter(X,y, marker='x', color='blue', label='observed')
    ax.plot(xx, gbr.predict(xx.reshape(-1,1)), color='green', label='gbr')
    ax.set_title(f"Base Learners: {n_learners}")
    ax.legend()

plt.tight_layout()
# plt.savefig('q1_alpha_0.1.png')
plt.show()
