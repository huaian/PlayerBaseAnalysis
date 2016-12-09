# Recursive Feature Elimination
import numpy as np
import pandas as pd
#RFE
from sklearn import datasets
import matplotlib.pyplot as plt
#RFE Mods
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

from sklearn import linear_model

from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier


f = open('player_data_plus.csv', 'r+')
lines = f.readlines()
stats = [line.replace('\n', '') for line in lines[0].split(', ')]
print(len(lines))
print(stats[1:])
all_player_data = [[float(data.replace('\n', '')) for data in line.split(', ')[1:]] for line in lines[1:]]
#print( all_player_data[0])
win_data = [int(float(line.split(', ')[0]) * 100) for line in lines[1:]]

all_player_data = np.array(all_player_data)
win_data = np.array(win_data)

model = LogisticRegression()
rfe = RFE(model, 1)
# print(win_data)
# print(dataset.target)
print(len(all_player_data[0]))
rfe= rfe.fit(all_player_data, win_data)
print(stats[1:])
print(rfe.support_)
print(rfe.ranking_)

finalStats=  stats[:]
for i in range(len(finalStats)):
    for rank in rfe.ranking_:
        if rank == i:
            print(finalStats[i])    

