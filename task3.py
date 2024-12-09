import pandas as pd  # this library will help to convet csv file to array
import numpy as np

# in our algorithm step two will be called whenever step 3 is done
def step2(work, alloc, rows, finish,reqarr):
    route = ""
    for i in range(rows):
        if not finish[i] and np.all(reqarr[i] <= work):
            work = work + alloc[i]
            finish[i] = True
            route = route + "P" + str(i + 1) + "-->"
            route = route + step2(work, alloc, rows, finish,reqarr)
    return route  # will return the safe route


def deadlockDetectionAndSafeRoute(allocMat, available, reqMat):
    rows, cols = allocMat.shape  # to get the dimension of the matrix
    work = np.array(available).astype(int)  # our matrix are str from pandas liberary so it must be converted to int
    safeRoute = ""  # initialzing the safe route
    finish = []  # initialzing an empty finsih array
    allArr = np.array(allocMat).astype(int)
    reqArr = np.array(reqMat).astype(int)
    # step 1
    for i in range(rows):
        finish_i = np.all(allArr[i] == 0)  # if row is full of zeros then finsih will be true otherwise false
        finish.append(finish_i)
    # step2,3
    for i in range(rows):
        if not finish[i] and np.all(reqArr[i] <= work):
            work = work + allArr[i]
            safeRoute = safeRoute + "P" + str(i + 1) + "-->" # it will add every ready process to the safe route
            finish[i] = True
            safeRoute = safeRoute + step2(work, allArr, rows, finish,reqArr)# to recheck every process after

    deadlock = False
    for i in range(rows):# to print deadlocked processes
        if not finish[i]:
            print("there are deadlock in P", (i + 1))
            deadlock = True

    if deadlock:
        print("there are deadlock in")
    else:
        #if there are no deadlock the safe route will be printed
        print("there are no deadlock in")
        print("safe route is " + safeRoute)

# this function will check if the dimentions of the two matrices and the vector correspnd to each other
def isDimentionConsistent(allocMat, availableMat, reqMat):
    allocRows, allocCols = allocMat.shape
    availableRows, availableCols = availableMat.shape
    reqRows, reqCols = reqMat.shape
    validN = (allocRows == reqRows)
    validM = (allocCols == availableCols == reqCols)
    return validN and validM

def main():
    #reading matrices from csv files
    allocationMatrix = pd.read_csv("Allocation.csv", header=None)
    available = pd.read_csv("Available.csv", header=None)
    requestMatrix = pd.read_csv("Request.csv", header=None)
    # i cropped the first row , colomn so that only the values are stored
    allocationMatrix = allocationMatrix.iloc[1:, 1:]
    requestMatrix = requestMatrix.iloc[1:, 1:]
    available = available.iloc[1:, :]

    if isDimentionConsistent(allocationMatrix, available, requestMatrix):
        print("the dimentions are consistent\n")
        deadlockDetectionAndSafeRoute(allocationMatrix, available, requestMatrix)
    else:
        print("the dimentions are not consistent")

if __name__ == "__main__":
    main()
