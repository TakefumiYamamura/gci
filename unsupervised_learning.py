# coding: utf8
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
import copy

a = np.random.random((10,5))+2
b = np.random.random((10,5))+5
c = np.random.random((10,5))+8
X = np.concatenate((a,b,c))

# p= pdist(X, metric="euclidean") #ユークリッド距離を採用する
Z = linkage(X, metric="euclidean", method="ward") #最小最短距離法をmethodで指定する

def center_weight(population):
  center = np.array([0,0,0,0,0])
  count = 0
  for x in population:
    center += x
    count += 1
  return center/count

def euclid(x,y):
  return np.linalg.norm(x-y)

def sum_of_square(population):
  center = center_weight(population)
  sum = 0
  for x in populatiion:
    sum += euclid(center, x)

def evaluation(x, y):
  sum_of_square(copy.deepcopy.(np.vstack((x,y))) - sum_of_square(x) - sum_of_square(y)

def ward(cluster):
  clusters_num = len(cluster)
  for i in range(clusters_num):
    for j in range(i + 1, clusters_num):
      evaluation(cluster[i], cluster[j])





ward(X)

# print p

# dendrogram(Z)

# plt.show()