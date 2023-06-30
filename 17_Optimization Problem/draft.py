import numpy as np
def Interior_Point(c,A,b):
    # 当输入的c,A,b有缺失值时，输出错误原因，函数执行结束
    if c.shape[0] != A.shape[1]:
        print("A和C形状不匹配")
        return 0
    if b.shape[0] != A.shape[0]:
        print("A和b形状不匹配")
        return 0
    # 初值的设置
    x=np.ones((A.shape[1],1)) # 将x的初值设为1
    v=np.ones((b.shape[0],1))  # 将v的初值设为1
    lam=np.ones((x.shape[0],1))  # 将lam的初值设为1
    one=np.ones((x.shape[0],1))
    mu=1 # 将mu的初值设为1
    n=A.shape[1]
    x_=np.diag(x.flatten()) # 将x转换为对角矩阵
    lam_=np.diag(lam.flatten()) # 将lam转换为对角矩阵
    # 初始的F，r=F
    r1=np.matmul(A,x)-b
    r2=np.matmul(np.matmul(x_,lam_),one)-mu*one
    r3=np.matmul(A.T,v)+c-lam
    r=np.vstack((r1,r2,r3))
    F=r
    # 求得r1、r2、r3的初始范数
    n1=np.linalg.norm(r1)
    n2=np.linalg.norm(r2)
    n3=np.linalg.norm(r3)
    # nablaF中零矩阵和单位阵的设置
    zero11=np.zeros((A.shape[0],x.shape[0]))
    zero12=np.zeros((A.shape[0],A.shape[0]))
    zero22=np.zeros((x.shape[0],A.shape[0]))
    zero33=np.zeros((A.shape[1],A.shape[1]))
    one31=np.eye(A.shape[1])
    tol=1e-8 # 设置最优条件的容忍度
    t=1
    alpha = 0.5
    while max(n1,n2,n3)>tol:
        # F的Jacobian矩阵
        nablaF = np.vstack((np.hstack((zero11, zero12, A))
                            , np.hstack((x_, zero22, lam_))
                            , np.hstack((-one31, A.T, zero33))))
        # F+nablaF@delta=0,解方程nablaF@delta=-r
        delta = np.linalg.solve(nablaF, -r)  # 解方程，求出delta的值
        delta_lam = delta[0:lam.shape[0], :]
        delta_v = delta[lam.shape[0]:lam.shape[0] + v.shape[0], :]
        delta_x = delta[lam.shape[0] + v.shape[0]:, :]
        # 更新lam、v、x、mu
        alpha=Alpha(c,A,b,lam,v,x,alpha,delta_lam,delta_v,delta_x)
        lam=lam+alpha*delta_lam
        v=v+alpha*delta_v
        x=x+alpha*delta_x
        x_ = np.diag(x.flatten())  # 将x转换为对角矩阵
        lam_ = np.diag(lam.flatten())  # 将lam转换为对角矩阵
        mu=(0.1/n)*np.dot(lam.flatten(),x.flatten()) #更新mu的值
        # 计算更新后的F
        r1 = np.matmul(A, x) - b
        r2 = np.matmul(np.matmul(x_, lam_), one) - mu * one
        r3 = np.matmul(A.T, v) + c - lam
        r = np.vstack((r1, r2, r3))
        F = r
        # 计算更新后F的范数
        n1 = np.linalg.norm(r1)
        n2 = np.linalg.norm(r2)
        n3 = np.linalg.norm(r3)
        t=t+1
        z=(c.T @ x).flatten()[0]
    print("x的取值",x.flatten())
    print('最优值为',z)

# 寻找alpha
def Alpha(c,A,b,lam,v,x,alpha,delta_lam,delta_v,delta_x):
    alpha_x=[]
    alpha_lam=[]
    for i in range(x.shape[0]):
        if delta_x.flatten()[i]<0:
            alpha_x.append(x.flatten()[i]/-delta_x.flatten()[i])
        if delta_lam.flatten()[i]<0:
            alpha_lam.append(lam.flatten()[i]/-delta_lam.flatten()[i])
    if len(alpha_x)==0 and len(alpha_lam)==0:
        return alpha
    else:
        alpha_x.append(np.inf)
        alpha_lam.append(np.inf)
        alpha_x = np.array(alpha_x)
        alpha_lam= np.array(alpha_lam)
        alpha_max = min(np.min(alpha_x), np.min(alpha_lam))
        alpha_k = min(1,0.99*alpha_max)
    return alpha_k

c = np.array([-5, -1, 0,0]).reshape(-1, 1)
A = np.array([[1, 1, 1, 0], [2, 0.5, 0, 1]])
b = np.array([5, 8]).reshape(-1, 1)
Interior_Point(c,A,b)