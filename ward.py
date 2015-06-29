# coding: utf8
from sklearn import datasets, cluster
import numpy as np
iris = datasets.load_iris()
data = iris.data
target = iris.target

# Ward(n_clusters=3)でクラスタリングしてみる。
#　クラスタリング結果（ラベル付与結果）は estimator.labels_ に保存される。
#　簡易評価として target との違いを目視チェック。
ward = cluster.Ward(n_clusters=3)
ward.fit(data)
print ward.labels_[::10]
print target[::10]
