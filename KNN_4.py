import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import math

test_x = pd.read_csv("test_x.txt", header=-1)
test_y = pd.read_csv("test_y.txt", header=-1)
train_x = pd.read_csv("train_x.txt", header=-1)
train_y = pd.read_csv("train_y.txt", header=-1)
train_y = train_y.values
test_y = test_y.values


def KNN(num):
    knn = KNeighborsClassifier(n_neighbors=11, metric='mahalanobis', p=math.log10(num))
    knn.fit(train_x, train_y)
    train_x_predict = knn.predict(train_x)
    train_x_predict = train_x_predict.reshape(-1, 1)
    error_index_train = np.nonzero(train_x_predict - train_y)[0]
    train_error_rate = (len(error_index_train) / len(train_x)) / 11

    test_x_predict = knn.predict(test_x)
    test_x_predict = test_x_predict.reshape(-1, 1)
    error_index_test = np.nonzero(test_x_predict - test_y)[0]
    test_error_rate = (len(error_index_test) / len(test_x)) / 11

    return train_error_rate, test_error_rate


num = 0.1
axes_x = []
train_error = []
test_error = []
while num < 1.1:
    [train_error_num, test_error_num] = KNN(num)
    train_error.append(train_error_num)
    test_error.append(test_error_num)
    axes_x.append(num)
    num = num + 0.1

plt.plot(1)
plt.subplot(211)
plt.scatter(axes_x, test_error, marker='.')
plt.ylim((0, 0.002))
plt.ylabel('test_error')
plt.subplot(212)
plt.scatter(axes_x, train_error, marker='.')
plt.ylim((0, 0.002))
plt.ylabel('train_error')
plt.show()