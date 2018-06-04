def loadData(filename):
    data = open(filename, 'r')

    X1 = []
    X2 = []
    X3 = []
    X4 = []
    X5 = []

    for line in data:
        line = line.strip('\n\r')
        input_data = line.split(',')

        X1.append(input_data[0])
        X2.append(input_data[1])
        X5.append(input_data[4])

    return (X1, X2, X5)


import pylab
import numpy


def plotData(X1, X2, X5):
    length = len(X1)
    figue = pylab.figure(1)
    ax = figue.add_subplot(111)
    # pylab.plot(X,Y,'rx')
    pylab.xlabel('X')
    pylab.ylabel('Y')
    if X5 == str(0):
        ax.scatter(X1, X2, c='r', marker='o')
    else:
        ax.scatter(X1, X2, c='g', marker='x')

    pylab.show()


(X1, X2, X5) = loadData('1.txt')
print(X5)
plotData(X1, X2, X5)
