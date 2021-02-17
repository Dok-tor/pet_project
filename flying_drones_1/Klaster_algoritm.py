"""
====================================
Demonstration of k-means assumptions
====================================

This example is meant to illustrate situations where k-means will produce
unintuitive and possibly unexpected clusters. In the first three plots, the
input data does not conform to some implicit assumption that k-means makes and
undesirable clusters are produced as a result. In the last plot, k-means
returns intuitive clusters despite unevenly sized blobs.
"""
# print(__doc__)

# Author: Phil Roth <mr.phil.roth@gmail.com>
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt

import sklearn.cluster
from sklearn.datasets import make_blobs

# plt.figure(figsize=(12, 12))

myList = []
fname = 'test_01.txt'
with open(fname) as f:
    for n, line in enumerate(f, 1):
        line = str(n) + " " + line
        line = line.rstrip('\n').strip().split()
        # print (n)
        # print (line)
        x_y = [int(line) for line in line]
        myList.append(x_y)

X = np.array(myList)

# n_samples = 1500
# random_state = 170
# X, y = make_blobs(n_samples=n_samples, random_state=random_state)

# KMeans
y_pred = sklearn.cluster.KMeans(n_clusters=1, random_state=0).fit(X)
# x = getattr(y_pred, 'cluster_centers_')
print(y_pred.cluster_centers_)
# plt.subplot(221)
# plt.scatter(X[:, 1], X[:, 2], c=y_pred, s=1)
# plt.title("KMeans\nFile: %s" % fname)

# print(type(y_pred))
# for i in range(100):
#     print(X[i], y_pred[i])

# MiniBatchKMeans
# y_pred = sklearn.cluster.MiniBatchKMeans(n_clusters=1000, random_state=0).fit_predict(X)
# print(type(y_pred))
# plt.subplot(222)
# plt.scatter(X[:, 0], X[:, 1], c=y_pred)
# plt.title("MiniBatchKMeans\nFile: %s" % fname)

# # Anisotropicly distributed data
# transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
# X_aniso = np.dot(X, transformation)
# y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_aniso)
#
# plt.subplot(222)
# plt.scatter(X_aniso[:, 0], X_aniso[:, 1], c=y_pred)
# plt.title("Anisotropicly Distributed Blobs")
#
# # Different variance
# X_varied, y_varied = make_blobs(n_samples=n_samples,
#                                 cluster_std=[1.0, 2.5, 0.5],
#                                 random_state=random_state)
# y_pred = KMeans(n_clusters=3, random_state=random_state).fit_predict(X_varied)
#
# plt.subplot(223)
# plt.scatter(X_varied[:, 0], X_varied[:, 1], c=y_pred)
# plt.title("Unequal Variance")
#
# # Unevenly sized blobs
# X_filtered = np.vstack((X[y == 0][:500], X[y == 1][:100], X[y == 2][:10]))
# y_pred = KMeans(n_clusters=3,
#                 random_state=random_state).fit_predict(X_filtered)
#
# plt.subplot(224)
# plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
# plt.title("Unevenly Sized Blobs")

plt.show()

