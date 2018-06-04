
# -*- coding:utf-8 -*-

"""
绘制箱体图
Created on 2017.09.04 by ForestNeo
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""
generate data from min to max
"""
def list_generator(number, min, max):
    dataList = list()
    for i in range(1, number):
        dataList.append(np.random.randint(min, max))
    return dataList

#generate 4 lists to draw
list1 = list_generator(100, 20, 80)
list2 = list_generator(100, 20, 50)
list3 = list_generator(100, 50, 100)
list4 = list_generator(100, 5, 60)

data = pd.DataFrame({
    "dataSet1":list1,
    "dataSet2":list2,
    "dataSet3":list3,
    "dataSet4":list4,
})

#draw
data.boxplot()
plt.ylabel("ylabel")
plt.xlabel("different datasets")
plt.show()


