import csv
import random
import math
import operator

# split the data into a training dataset and test dataset in ratio of 67/33
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    # open the file
    # data format:
    # sepal length, sepal width, petal length, petal width, classification
    # e.g 
    # 5.9, 3.0, 5.1, 1.8, Iris-virginica
    with open(filename, 'rb') as csvfile:
        # returns a reader object which will iterate over lines
        lines = csv.reader(csvfile)
        # dataset is a list of all data, where each item is a line as list
        dataset = list(lines)
        for x in range(len(dataset) - 1):
            # convert the content to float
            for y in range(len(iv)):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


# get k nearest neighbors of the <array><num> testInstance among <array><array>
# trainingSet
def getNeighbors(trainingSet, testInstance, k):
    distance = []
    length = len(testInstance)

    for x in range((len(trainingSet))):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distance.append((trainingSet[x], dist))
    # sort based on the the item at index 1 i.e the distance
    distance.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distance[x][0])
    return neighbors


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

neighbors = [[1,1,1,'b'], [2,2,2,'a'], [3,3,3,'b']]
response = getResponse(neighbors)
print(response)

iv = ["sepal length", "sepal width", "petal length", "petal width"]
trainingSet = []
testSet = []
loadDataset('iris.data', 0.66, trainingSet, testSet)

print("Train: " + repr(len(trainingSet)))
print("Train: " + repr(len(testSet)))
