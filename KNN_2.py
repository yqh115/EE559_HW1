import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import confusion_matrix

test_x = pd.read_csv("test_x.txt", header=-1)
test_y = pd.read_csv("test_y.txt", header=-1)
train_x = pd.read_csv("train_x.txt", header=-1)
train_y = pd.read_csv("train_y.txt", header=-1)
train_y = train_y.values
test_y = test_y.values


def KNN(num):
    knn = KNeighborsClassifier(n_neighbors=num)
    knn.fit(train_x, train_y)
    train_x_predict = knn.predict(train_x)
    train_x_predict = train_x_predict.reshape(-1, 1)
    error_index_train = np.nonzero(train_x_predict - train_y)[0]
    train_error_rate = (len(error_index_train) / len(train_x)) / num

    test_x_predict = knn.predict(test_x)
    test_x_predict = test_x_predict.reshape(-1, 1)
    error_index_test = np.nonzero(test_x_predict - test_y)[0]
    test_error_rate = (len(error_index_test) / len(test_x)) / num

    return train_error_rate, test_error_rate, test_x_predict


num = 19
[train_error_num, test_error_num, test_predict] = KNN(num)
confusion_matrix(test_y, test_predict)
print(confusion_matrix)
