import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn



def rivit(data):
    numberOfRows = len(data)
    numberOfRows = int(numberOfRows)
    return numberOfRows



def dataprocess(numberOfRows,data):
    datamatrix = np.zeros((numberOfRows,3))
    datamatrix[:,0] = data.values[0::,5]
    datamatrix[:,1] = data.values[0::,6]
    datamatrix[:,2] = data.values[0::,7]
    print(datamatrix)
    
    return datamatrix

def randomdata():
    random = np.random.randint(min, max, size=(6,3))
    return random

def kmeans(numberOfRows, random, datamatrix):
    for z in range (10):
        counts = np.zeros(6)
        avgDistance = np.zeros((6,3))
        dist1 = np.zeros(6)
        centerPointCumulativeSum = np.zeros((6,3))

        for i in range(numberOfRows):
            for j in range(6):
                dist = np.abs(np.sqrt(np.power((random[j,0]- datamatrix[i,0]),2) + 
                               np.power((random[j,1]- datamatrix[i,1]),2) + 
                               np.power((random[j,2]- datamatrix[i,2]),2)))
                dist1[j] = dist
            p = np.argmin(dist1) 
            counts[p] += 1
            centerPointCumulativeSum[p,0:3] += datamatrix[i,0:3]

        for a in range(6):
            if (counts[a]==0):
                avgDistance[a] = np.random.randint(min, max, size=3)

            else:
                avgDistance[a] = (centerPointCumulativeSum[a]/counts[a])
                avgDistance = np.around(avgDistance, 2)

        random = avgDistance
        print(avgDistance, "\n")



    fig = plt.figure()
    ax = plt.axes(projection='3d')
    for i in range(numberOfRows):
        ax.scatter(datamatrix[:,0],datamatrix[:,1],datamatrix[:,2])
    for i in range(6):
        ax.scatter(avgDistance[:,0],avgDistance[:,1],avgDistance[:,2],marker='*', color='red', s=200)



    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    plt.show()


                
        
        
        


if __name__ == "__main__":

    filename = 'C:/Koulu (Tietotekniikka)/anturidataa/dataa.csv'
    data = pd.read_csv(filename, delimiter=";")
    
    global min
    global max


    min = np.min(data.values[0::,5:7])
    max = np.max(data.values[0::,5:7])
    print(min, max)
    
    
    numberOfRows = rivit(data)
    random = randomdata()
    datamatrix = dataprocess(numberOfRows, data)
    kmeans(numberOfRows, random, datamatrix)





