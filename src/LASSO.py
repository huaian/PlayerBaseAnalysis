
# coding: utf-8

# In[83]:
from sklearn import linear_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("player_data_plus.csv",sep=', ', engine='python')
X, y= df[[col for col in df.columns if col not in ['Player Id', 'Player Name', 'Champions Played', 'winLossRatio']]], np.log(df.winLossRatio).reshape(-1,1)
print(df.describe())
# print(X1)
# print(type(X1))



X = np.hstack((np.ones_like(y), X))

# print(y)
# print(X)

# for num in X[0]:
#     print(num)
#     print(type(num))
# print(type(X))

def objective(X, y, w, reg = 1e-6):
    # Distance between our guess and the true value
    err = X @ w - y
    # Square it
    err = float(err.T @ err)
    # ||w|| = w.sum()
    # if (err + reg * np.abs(w).sum())/len(y) < 100:
    #     print((err + reg * np.abs(w).sum())/len(y))
    return (err + reg * np.abs(w).sum())/len(y)

def grad_objective(X, y, w):
    return X.T @ (X @ w - y)/len(y)

def prox(x, gamma):
    x[abs(x) <= gamma] = 0
    x[x > gamma] = x[x > gamma] - gamma
    x[x < -gamma] = x[x < -gamma] + gamma
    return x

def lasso_grad( 
    X, y, reg=1e-6, lr=1e-3, tol=1e-6,
    max_iters=350, batch_size=256, eps=1e-5,
    verbose=True, print_freq=250,
    ):
    y = y.reshape(-1,1)
    w = np.linalg.solve(X.T @ X, X.T @ y)
    #print(type(w))
    ind = np.random.randint(0, X.shape[0], size=batch_size)
    obj = [objective(X[ind], y[ind], w, reg = reg)]
    gradient = grad_objective(X[ind], y[ind], w)
    while (len(obj) -1 <= max_iters) and (np.linalg.norm(gradient) > tol):
        if verbose and (len(obj) - 1) % print_freq == 0:
            print("[i] objective: {}. sparsity = {:0.2f}".format(len(obj)-1, obj[-1], (np.abs(w) < reg*lr).mean()))

        ind = np.random.randint(0, X.shape[0], size = batch_size)
        gradient = grad_objective(X[ind], y[ind], w)
        w = prox(w - lr * gradient, reg * lr)
        obj.append((objective(X[ind], y[ind], w, reg=reg)))
    if verbose:
        print("[i={}] done. sparsity = {:0.2f}".format(len(obj)-1, (np.abs(w) < reg*lr).mean()))
    return w, obj

def lasso_path( X, y, reg_min = 1e-8, reg_max = 10, regs = 10, **grad_args):
    w = np.zeros((X.shape[1], regs))
    tau = np.linspace(reg_min, reg_max, regs)
    for i in range(regs):
        w[:,i] = lasso_grad(X, y, reg = 1/tau[i], max_iters = 1000, batch_size = 1024, **grad_args)[0].flatten()
    return tau, w

tau, w = lasso_path(X, y, reg_min=1e-10, reg_max=2, regs=10, lr=1e-3)
p = plt.plot(tau, w.T )
plt.title("Lasso Path")
plt.xlabel("$\tau = \lambda^{-1}$")
plt.ylabel("$w_i$")
plt.savefig("lol_lasso_path.pdf")
##find most important features
print(np.array(df.columns)[np.argsort(-w[:,9])[:5]+1])



lr = 1e-12
reg = 1e5
w, obj = lasso_grad(
X, y, reg=1e5, lr=1e-12, eps=1e-2,
max_iters=500, batch_size=1024,
verbose=True, print_freq= 250,
)
plt.title("LOL Lasso Objective Convergence ($\lambda={}$)".format(reg))
plt.ylabel("Stochastic Objective")
plt.xlabel("Iteration")
plt.plot(obj)
plt.show()




# In[ ]:



