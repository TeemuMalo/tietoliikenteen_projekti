import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rivit(data):
    numberOfRows = len(data)
    numberOfRows = int(numberOfRows)
    return numberOfRows

def dataprocess(numberOfRows,data):
    datamatrix = np.zeros((numberOfRows,3))
    datamatrix[:,0] = data.values[0::,5]
    datamatrix[:,1] = data.values[0::,6]
    datamatrix[:,2] = data.values[0::,7]
    position = data.values[0::,9]
    print(datamatrix)
<<<<<<< HEAD
    return datamatrix
=======
    return datamatrix, position
>>>>>>> 602d4522ddc23bcae61e105a76866d3e85f2d60c

def randomdata():
    random = np.random.randint(min, max, size=(6,3))
    return random

def kmeans(numberOfRows, random, datamatrix,position):
    for z in range (10):
        flag = np.zeros(6)
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
            flag[p] = position[i]
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
    
    #plt.show()

    headerData = avgDistance

<<<<<<< HEAD
    with open('keskipisteet.h', 'w') as f:
        line = "float w[3][6] = {"
=======
    with open('C:/git repot/tietoliikenteen_projekti/TransmitterOpiskelijoille/keskipisteet.h', 'w') as f:
        line = "float w[6][6] = {"
>>>>>>> 602d4522ddc23bcae61e105a76866d3e85f2d60c
        for i in range(5):
            line = line + "{"
            outputThis = np.array2string(headerData[i,:],precision=2,separator=',')
            line = line + outputThis[1:len(outputThis)-1]
<<<<<<< HEAD
=======
            line = line + "," + str(int(flag[i]))
>>>>>>> 602d4522ddc23bcae61e105a76866d3e85f2d60c
            line = line + "},"
        outputThis = np.array2string(headerData[5,:],precision=3,separator=',')
        line = line + "{"
        line = line + outputThis[1:len(outputThis)-1]
<<<<<<< HEAD
=======
        line = line + "," + str(int(flag[5]))
>>>>>>> 602d4522ddc23bcae61e105a76866d3e85f2d60c
        line = line + "}"
        line = line + "};"
        f.write(line)
        f.write('\n')
    f.close()



if __name__ == "__main__":

    filename = 'C:/Koulu (Tietotekniikka)/anturidataa/dataa.csv'
    data = pd.read_csv(filename, delimiter=";")
    
    global min
    global max


    min = np.min(data.values[0::,5:7])
    max = np.max(data.values[0::,5:7])
    #print(min, max)
    
    
    numberOfRows = rivit(data)
    random = randomdata()
    datamatrix, position = dataprocess(numberOfRows, data)
    kmeans(numberOfRows, random, datamatrix, position)





