# coding: utf8
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist
import scipy
import matplotlib.pyplot as plt
import copy
import random
random.seed(0)
a = np.random.random((10,5))+2
b = np.random.random((10,5))+5
c = np.random.random((10,5))+8
X = np.concatenate((a,b,c))

# p= pdist(X, metric="euclidean") #ユークリッド距離を採用する
# print plt
# Z = linkage(X, metric="euclidean", method="ward") #最小最短距離法をmethodで指定する
# print plt
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
  for x in population:
    sum += euclid(center, x)
  return sum

def evaluation(x, y):
  return sum_of_square(np.vstack((x,y)) - sum_of_square(x) - sum_of_square(y) )

def ward(cluster):
  clusters_num = len(cluster)
  cluster_label = []
  Z = []
  for i in range(clusters_num):
    cluster_label.append({"label":i, "root_num":1})
  # print cluster_label
  count = clusters_num
  while clusters_num != 1:
    count += 1
    mini_num = 100010001
    for i in range(clusters_num):
      for j in range(i + 1, clusters_num):
        # print cluster
        # print cluster[i]
        # print j
        # print len(cluster)
        # print cluster[j]
        eva = evaluation(cluster[i], cluster[j])
        if eva < mini_num:
          mini_num = eva
          delete_i, delete_j = i, j
          mini_cluster_x = cluster_label[i]["label"]
          mini_cluster_y = cluster_label[j]["label"]
          mini_root_num = cluster_label[i]["root_num"] + cluster_label[j]["root_num"]
        # print "%i %i %f " %(i, j, evaluation(cluster[i], cluster[j]))
    # Z.appned( np.array([mini_cluster_x, mini_cluster_y, mini_num, mini_root_num]) )
    Z.append([mini_cluster_x, mini_cluster_y, mini_num, mini_root_num])
    # print cluster
    cluster_stash = cluster.tolist()
    # print cluster_stash
    if mini_root_num == 2:
      z = []
      z.append(cluster_stash[delete_i])
      z.append(cluster_stash[delete_j])
    else:
      if not isinstance(cluster_stash[delete_i][0], list):
        cluster_stash[delete_i] = [cluster_stash[delete_i]]
      if not isinstance(cluster_stash[delete_j][0], list):
        cluster_stash[delete_j] = [cluster_stash[delete_j]]
      # if  isinstance(cluster_stash[delete_i], list) && isinstance(cluster_stash[delete_j], list):
      z = cluster_stash[delete_i]
      z.extend(cluster_stash[delete_j])
    cluster_stash.append(z)
    cluster_stash.pop(delete_i)
    cluster_stash.pop(delete_j - 1)
    # cluster_stash.append(z)
    cluster_label.pop(delete_i)
    cluster_label.pop(delete_j - 1)
    cluster_label.append({"label":count, "root_num":mini_root_num})
    cluster = np.array(cluster_stash)
    # print cluster
    # print cluster_label
    clusters_num = len(cluster)
  return np.array(Z)

Z = ward(X)
# print p
print Z
# print len(Z)
dendrogram(Z)
plt.show()

