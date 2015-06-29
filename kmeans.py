# coding: utf8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import random
import copy

def k_means_tool(X, clusters_num):
  #ランダムにクラスをわける
  class_label = []
  #最初の適当なクラス分け
  for j in range(0, len(X)):
    class_label.append(random.randrange(0,clusters_num))
  print class_label
  flag = True
  count = 0
  while flag:
    #グループの中心を求める
    V = [] #クラスタの中心
    for i in range(0, clusters_num):
      # V.append([0,0])
      center = np.array([0,0])
      count_clusters = 0
      for j in range(0, len(X)):
        if class_label[j] == i:
          center = center + np.array(X[j])
          count_clusters += 1
          # V[i] = [x + y for (x, y) in zip(V[i], X[j])]
      V.append(copy.deepcopy(list(center/count_clusters)))
      # V[i] = map(lambda n:n/len(X), V[i])
    print V #重心を計算
    #V[i]に平均入りました
    #さっきのグループ分けは適当だったから、一番近いグループの中心に基づいて再度グループ分けし直すよ。
    flag = False
    for j in range(0, len(X)):
      mini_distance = np.linalg.norm(np.array(V[class_label[j]])-np.array(X[j]))
      # print mini_distance
      for i in range(0, clusters_num):
        # np.linalg.norm(np.array(a)-np.array(b))
        # print mini_distance > np.linalg.norm(np.array(V[i])-np.array(X[i]))
        if mini_distance > np.linalg.norm(np.array(V[i]) - np.array(X[j])) :
          flag = True #更新があった
          mini_distance = np.linalg.norm(np.array(V[i]) - np.array(X[j]))
          class_label[j] = copy.deepcopy(i) # 一番近い重心の色に変わる
    count += 1
    if count > 5 :
      flag = False
    print class_label
  return np.array(X), np.array(class_label)




a=np.random.random((100,2))+2
b=np.random.random((100,2))+2
c=np.random.random((100,2))+2
X=np.concatenate((a,b,c))

print len(X)
# k_means= KMeans(init='random', n_clusters=3) #init：初期化手法、n_clusters=クラスタ数を指定
# k_means.fit(X)
X, Y = k_means_tool(X, 3)

print Y
# Y.append()
# Y=k_means.labels_  #得られた各要素のラベル

# plt.figsize(10,5) なんかエラー出るよ
# plt.scatter(*zip(*X), c = k_means.labels_, vmin=0, vmax=2, s=12)
plt.scatter(*zip(*X), c = Y, vmin=0, vmax=2, s=12)

plt.show()







