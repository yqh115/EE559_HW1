import matplotlib.pyplot as plt
import numpy as np


def loadData(filename1, filename2):
    a = np.loadtxt(filename1)
    b = np.loadtxt(filename2)

    all_data = np.array([a, b])

    bplot = plt.boxplot(all_data,
                notch=False, # box instead of notch shape
                sym='bs',    # red squares for outliers
                vert=True,
                patch_artist = True)

    colors = ['red', 'green']

    for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)

    # adding horizontal grid lines

    # add x-tick labels
    plt.xticks([y+1 for y in range(len(all_data))], ['Class_0', 'Class_1'])
    plt.xlabel('Skewness')
    #plt.setp(bplot1, xticklabels=['class_0', 'class_1'])
    plt.show()


loadData('Skewness_0', 'Skewness_1')
