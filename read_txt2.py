import pylab
import numpy

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

        X1.append(input_data[1])
        X2.append(input_data[3])
        X3.append(input_data[3])
        X4.append(input_data[3])
        X5.append(input_data[4])


        figue = pylab.figure('Curtosis2')
        ax = figue.add_subplot(111)
        # pylab.plot(X,Y,'rx')
        pylab.xlabel('Curtosis2')
        #pylab.ylabel('X4')

        if input_data[4] == str(0):
            ax.scatter(input_data[2], 0, c='r', marker=',')
        else:
            ax.scatter(input_data[2], 1, c='g', marker=',')


    pylab.show()

loadData('1.txt')


