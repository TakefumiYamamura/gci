# coding: utf8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import random

def k_means_tool(X, clusters_num):
  #ランダムにクラスをわける
  # random.shuffle(X)
  class_label = []
  #最初の適当なクラス分け
  for i in range(0, clusters_num):
    for j in range(0, len(X)/clusters_num):
      class_label.append(i)
  print class_label
  flag = True
  count = 0
  while flag:
    #グループの中心を求める
    V = [] #クラスタの中心
    for i in range(0, clusters_num):
      V.append([0,0])
      for j in range(0, len(X)):
        if class_label[j] == i:
          V[i] = [x + y for (x, y) in zip(V[i], X[i])]
      V[i] = map(lambda n:n/len(X), V[i])
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
          class_label[j] = i # 一番近い重心の色に変わる
    count += 1
    if count >0 :
      flag = False
    print class_label
  return np.array(X), np.array(class_label)




a=np.random.random((100,2))+2
b=np.random.random((100,2))+5
c=np.random.random((100,2))+8
X=np.concatenate((a,b,c))

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







