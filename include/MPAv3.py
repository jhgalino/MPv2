import copy


def addDistance(names: list, score: int):
    for name in names:
        name.append(abs(score - name[1]))
    return names


def sort(listToSort: list):
    return sorted(
        sorted(listToSort, key=lambda x: x[0], reverse=True),
        key=lambda x: (x[2], x[1], len(x[0])),
    )


def extraFriend(listOfNames: list, almost: list, distance: int, barkada: list):
    closestList = list(filter(lambda x: x[2] == distance, listOfNames))
    closestList = sort(closestList)
    if len(closestList) == 0:
        print("{}, {}".format(almost[0], "almost"))
    else:
        if closestList[0][0] in barkada:
            print(almost[0])
        else:
            print("{}, {}".format(almost[0], closestList[0][0]))


names = []
score = int(input())
barkadaSize = int(input())
numberOfNames = int(input())
for n in range(numberOfNames):
    name = input().split()
    name[1] = int(name[1])
    names.append(name)

namesWithScore = addDistance(copy.deepcopy(names), score)
namesWithScore = sort(namesWithScore)

distanceToClosest = namesWithScore[0][2]

if len(namesWithScore) > barkadaSize:
    almostFriend = namesWithScore[barkadaSize]
    namesWithAlternate = addDistance(copy.deepcopy(names), almostFriend[1])
    namesWithAlternate = list(
        filter(lambda x: x[0] != almostFriend[0], namesWithAlternate)
    )
    namesWithAlternate = sort(namesWithAlternate)

barkadaList = [x[0] for x in namesWithScore[:barkadaSize]]

for name in barkadaList:
    print(name)

if len(namesWithScore) > barkadaSize:
    extraFriend(namesWithAlternate, almostFriend, distanceToClosest, barkadaList)

