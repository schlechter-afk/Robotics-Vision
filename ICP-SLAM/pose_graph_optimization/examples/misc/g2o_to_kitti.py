from sys import argv, exit
import numpy as np

def readTxt(filename):
    f = open(filename, 'r')
    A = f.readlines()
    f.close()

    X = []
    Y = []
    THETA = []

    for i, line in enumerate(A):
        if(i % 1 == 0):
            (x, y, theta) = line.split()
            X.append(float(x))
            Y.append(float(y))
            THETA.append(np.radians(float(theta.rstrip('\n'))))

    return X, Y, THETA

def readG2o(fileName):
    f = open(fileName, 'r')
    A = f.readlines()
    f.close()

    X = []
    Y = []
    THETA = []

    for line in A:
        if "VERTEX_SE2" in line:
            (ver, ind, x, y, theta) = line.split()
            X.append(float(x))
            Y.append(float(y))
            THETA.append(float(theta.rstrip('\n')))

    X_temp = X
    Y_temp = Y
    X = [y for y in Y_temp]
    Y = [-x for x in X_temp]

    return (X, Y, THETA)

def getKitti(X, Y, THETA):
    A = np.zeros((len(X),12))

    for i in range(len(X)):
        R = np.array([[np.cos(THETA[i]), -np.sin(THETA[i]), 0],[np.sin(THETA[i]), np.cos(THETA[i]), 0], [0, 0, 1]])
        T = np.identity(4)
        T[0:3,0:3] = R
        T[0, 3] = X[i]
        T[1, 3] = Y[i]
        T[3, 3] = 1
        A[i] = T[0:3, :].reshape(1,12)
    return A

X,Y,THETA = readG2o(argv[1])
kit = getKitti(X,Y,THETA)

np.savetxt(argv[2], kit, delimiter=" ")