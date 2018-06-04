import matplotlib.pyplot as plt
import numpy as np


def loadData(filename1, filename2):
    a = np.loadtxt(filename1)
    b = np.loadtxt(filename2)

    bplot1 = a.boxplot(all_data,
                             vert=True,  # vertical box aligmnent
                             patch_artist=True)  # fill with color
    bplot2 = b.boxplot(all_data,
                             vert=True,  # vertical box aligmnent
                             patch_artist=True)  # fill with color

    boxprops_0 = dict(linestyle='-', linewidth=3, color='red')
    flierprops_0 = dict(marker='o', markerfacecolor='red', markersize=12,
                        linestyle='none')
    plt.boxplot(a, boxprops=boxprops_0, flierprops=flierprops_0, patch_artist=True)


    boxprops_1 = dict(linestyle='-', linewidth=3, color='green')
    flierprops_1 = dict(marker='x', markerfacecolor='green', markersize=12,
                        linestyle='none')
    plt.boxplot(b, boxprops=boxprops_1, flierprops=flierprops_1, patch_artist=True)

    colors = ['pink', 'lightblue', 'lightgreen']
    for bplot in (bplot1, bplot2):
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
    plt.xlabel('Entropy')
    plt.show()
    #plt.savefig("Skewness.jpg")

loadData('Entropy_0', 'Entropy_1')
