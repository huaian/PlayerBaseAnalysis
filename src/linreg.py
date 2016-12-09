import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

def linreg(X, y, reg=0.0):
    eye = np.eye(X.shape[1])
    eye[0,0] = 0.
    return np.linalg.solve( X.T @ X + reg * eye, X.T @ y )


df = pd.read_csv('player_data_plus.csv',sep=', ', engine='python')

# do train/test/validation split 
df['cohort'] = 'train'
#Splits up data
df.iloc[int(0.666*len(df)):int(0.833*len(df)),-1] = 'validation'
df.iloc[int(0.833*len(df)):,-1] = 'test'
print(df.describe())
X_train = df[df.cohort == 'train'][[col for col in df.columns if col not in ['cohort', 'Player Id', 'Player Name', 'Champions Played', 'winLossRatio']]]
y_train = df[df.cohort == 'train'].winLossRatio.reshape(-1,1)
X_val = df[df.cohort == 'validation'][[col for col in df.columns if col not in ['cohort', 'Player Id', 'Player Name', 'Champions Played', 'winLossRatio']]] 
y_val = df[df.cohort == 'validation'].winLossRatio.reshape(-1,1)

X_test = df[df.cohort == 'test'][[col for col in df.columns if col not in ['cohort', 'Player Id', 'Player Name', 'Champions Played', 'winLossRatio']]] 
y_test = df[df.cohort == 'test'].winLossRatio.reshape(-1,1)

X_train = np.hstack((np.ones_like(y_train), X_train))
X_val = np.hstack((np.ones_like(y_val), X_val))
X_test = np.hstack((np.ones_like(y_test), X_test))

theta_optimal = linreg(X_train, y_train, reg = 0.0)
theta_validation = linreg(X_val, y_val, reg = 0.0)
theta_test = linreg(X_test, y_test, reg = 0.0)
# print(theta_test)
# print(theta_optimal)
# print(theta_validation)

print(np.sqrt(np.mean((y_train - X_train @ theta_optimal)**2)))

print(np.sqrt(np.mean((y_test - X_test @ theta_test)**2)))
print(np.sqrt(np.mean((y_val - X_val @ theta_validation)**2)))

# print(y_train)
# print(X_train[0])
print(y_train[0] - X_train[0].T @ theta_optimal)
plt.title("Validation Set Metrics")
plt.xlabel = "RMSE"
plt.ylabel = "Regularization Term"
earl = []
lam = []

r = 100
delI = 0.1
i = -1 * r
while (i < r):
    theta_test = linreg(X_train, y_train, reg = i)
    res = X_train @ theta_test
    err = np.sqrt(np.mean((y_val - X_val @ theta_test)**2))
    #print(err)
    earl.append(err)
    lam.append(i)
    i += delI
print(min(earl))
print(earl.index(min(earl)))
print(lam[earl.index(min(earl))])
plt.plot(lam, earl)
plt.show()
print(theta_validation)
print(theta_test)

