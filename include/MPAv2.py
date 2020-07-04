# names[index][0] is name, [1] is score, [2] is distance
def checkIfSameScore(names: list):
    n = 1
    while n <= len(names) - 1:
        if int(names[n][1]) == int(names[n - 1][1]):
            return True
            break
        n += 1
    return False


def addDistance(listOfNames: list, score: int):
    for i in listOfNames:
        distance = abs(int(score) - int(i[1]))
        i.append(distance)
    return listOfNames


# check if name earlier in list is longer
def checkLongerName(name1: str, name2: str):
    if len(name1) > len(name2):
        return True
    else:
        return False


# names[index][0] is name, [1] is score, [2] is distance
def sortByDistance(listOfNames: list):
    listOfNames = sorted(listOfNames, key=lambda x: (x[2], x[1]))
    index = 1
    while index <= len(listOfNames) - 1:  # check if name earlier in list is longer
        if listOfNames[index][1] == listOfNames[index - 1][1]:
            if checkLongerName(listOfNames[index - 1][0], listOfNames[index][0]):
                # swap
                tempHolder = listOfNames[index - 1]
                listOfNames[index - 1] = listOfNames[index]
                listOfNames[index] = tempHolder
            else:
                # use reverse lexicographical order
                if listOfNames[index][0] > listOfNames[index - 1][0]:
                    tempHolder = listOfNames[index - 1]
                    listOfNames[index - 1] = listOfNames[index]
                    listOfNames[index] = tempHolder
        index += 1
    return listOfNames


def sortByDistance2(listOfNames: list):
    listOfNames = sorted(listOfNames, key=lambda x: (x[3], x[1]))
    index = 1
    while index <= len(listOfNames) - 1:  # check if name earlier in list is longer
        if listOfNames[index][1] == listOfNames[index - 1][1]:
            if checkLongerName(listOfNames[index - 1][0], listOfNames[index][0]):
                # swap
                tempHolder = listOfNames[index - 1]
                listOfNames[index - 1] = listOfNames[index]
                listOfNames[index] = tempHolder
            else:
                # use reverse lexicographical order
                if listOfNames[index][0] > listOfNames[index - 1][0]:
                    tempHolder = listOfNames[index - 1]
                    listOfNames[index - 1] = listOfNames[index]
                    listOfNames[index] = tempHolder
        index += 1
    return listOfNames


# expectedFriend[0] is name, [1] is score, [2] is distance
def findExtraFriend(names: list, scoreOfFriend: int, expectedCloseness: int):
    newNames = addDistance(names, scoreOfFriend)
    newNames = sortByDistance2(newNames)
    expectedFriend = newNames[1]
    if expectedFriend[3] == expectedCloseness:
        return expectedFriend[0]
    else:
        return "almost"


listNames = []
actualBarkada = []
score = int(input())
barkadaSize = int(input())
numberOfNames = int(input())
for n in range(numberOfNames):
    listNames.append(input().split())

tempBarkada = addDistance(listNames, score)
barkadaList = sortByDistance(tempBarkada)

for n in range(barkadaSize):
    actualBarkada.append(barkadaList[n][0])
almostBarkada = barkadaList[barkadaSize]
extraFriend = findExtraFriend(listNames, almostBarkada[1], barkadaList[0][2])
if extraFriend in actualBarkada:
    actualBarkada.append(almostBarkada[0])
    for name in actualBarkada:
        print(name)
else:
    for name in actualBarkada:
        print(name)
    print("{}, {}".format(almostBarkada[0], extraFriend))
