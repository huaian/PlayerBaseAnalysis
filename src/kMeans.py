import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

def kMeans(lst, N, maxiters = 1000 ):
    # print(lst)
    numFeatures = len(lst[0])

    # centroids = np.random.choice(len(lst), N)
    # centroids = [lst[data] for data in centroids]
    centroids = [[random.random() * 500 + 0.5 for x in range(len(lst[0]))] for cen in range(N)]
    # print(centroids)
    iterations = 0
    oldCentroids = []

    while (iterations < maxiters and not shouldStop(oldCentroids, centroids)):
        oldCentroids = centroids
        iterations += 1
        print(iterations)
        
        labels = assignToCentroid(lst, centroids)
        # print(centroids)
        centroids = getCentroids(lst, labels, N)
        print(centroids)
        # print(len(centroids))
    labels = assignToCentroid(lst, centroids)
    return centroids, labels

def getDistance( p1, p2):
    d= 0
    for ind in range(len(p1)):
        d += (p1[ind] - p2[ind])**2

    return np.sqrt(d)

def assignToCentroid(lst, centroids):
    centroidL = [[] for x in centroids]
    for point in lst:
        # print(point)
        # print(centroids)
        closestCentroid = [getDistance(x, point) for x in centroids]

        closestCentroid = closestCentroid.index(min(closestCentroid))
        centroidL[closestCentroid].append(point)

        # print(centroidL[0])
    return centroidL

def getCentroids(lst, labels, N):
    newCentroidL = []
    # print(newCentroidL )
    # print(labels)
    for group in labels:
        if group != [] and len(group) > 10:
            # print(type(group))
            # newCentroid = [sum([data[i] for data in group]) for i in range(len(lst[0]))]
            newCentroid = [0 for x in range(len(lst[0]))]
            for vec in group:
                for point in range(len(vec)):
                    newCentroid[point] += vec[point]
            # print("Adding Centroid")
            # print(newCentroid)
            newCentroid = [val/len(group) for val in newCentroid]

        else:
            newCentroid = [random.random() * 500 + 50 for x in range(len(lst[0]))] 
        # print(newCentroid)
        newCentroidL.append(newCentroid)
        # print(newCentroidL)
    return newCentroidL

def shouldStop(oldCentroids, newCentroids):
    diff = 0
    # print("Len(Centroid) {0}".format(len(newCentroids)))
    for cent in newCentroids:
        if cent not in oldCentroids:
            diff += 1
    print("Centroid difference {0}".format(diff))
    return oldCentroids == newCentroids

f = open('player_data_plus.csv', 'r+')
lines = f.readlines()
stats = [line.replace('\n', '') for line in lines[0].split(', ')]
# print(len(lines))
# print(stats[1:])
all_player_data = [[float(data.replace('\n', '')) for data in line.split(', ')] for line in lines[1:]]
#print( all_player_data[0])
win_data = [int(float(line.split(', ')[0]) * 100) for line in lines[1:]]
# all_player_data = [ [1,2,3], [4,5,6], [1,6,4], [5,2,6], [5,6,7]]
res, labels = kMeans(all_player_data, 3)

for player in res:
    print("Player:")
    for stat in range(len(stats)):
        print(stats[stat], player[stat])

for thing in labels:
    print()
    print(len(thing))
# print(stats)
