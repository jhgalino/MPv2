import copy


class RelationshipCircle:
    def __init__(self, listOfNames: list, centerScore: int, size: int):
        self.listOfNames = listOfNames
        self.centerScore = centerScore
        self.size = size
        self.barkada = []

    def addDistance(self):
        for name in self.listOfNames:
            distance = abs(self.centerScore - int(name[1]))
            name.append(distance)

    def sortByDistance(self):
        self.listOfNames = sorted(self.listOfNames, key=lambda x: x[2])
        # print(self.listOfNames)

    def sortByScore(self):
        for n in range(1, len(self.listOfNames)):
            position = n
            current = self.listOfNames[position]
            previous = self.listOfNames[position - 1]
            while current[2] == previous[2]:
                if current[1] < previous[1]:
                    tempHolder = current
                    self.listOfNames.pop(position)
                    self.listOfNames.insert(position - 1, tempHolder)
                    position -= 1
                    try:
                        current = self.listOfNames[position]
                        previous = self.listOfNames[position - 1]
                    except Exception:
                        break
                else:
                    break
        # print(self.listOfNames)

    def sortByName(self):
        for n in range(1, len(self.listOfNames)):
            position = n
            current = self.listOfNames[position]
            previous = self.listOfNames[position - 1]
            while current[1] == previous[1]:
                if len(current[0]) < len(previous[0]):
                    tempHolder = current
                    self.listOfNames.pop(position)
                    self.listOfNames.insert(position - 1, tempHolder)
                    position -= 1
                    try:
                        current = self.listOfNames[position]
                        previous = self.listOfNames[position - 1]
                    except Exception:
                        break
                elif current[0] > previous[0]:
                    tempHolder = current
                    self.listOfNames.pop(position)
                    self.listOfNames.insert(position - 1, tempHolder)
                    position -= 1
                    try:
                        current = self.listOfNames[position]
                        previous = self.listOfNames[position - 1]
                    except Exception:
                        break
                else:
                    break
        # print(self.listOfNames)

    def addToBarkada(self):
        for name in self.listOfNames:
            if len(self.barkada) != self.size:
                self.barkada.append(name)


names = []
score = int(input())
barkadaSize = int(input())
numberOfNames = int(input())
for n in range(numberOfNames):
    name = input().split()
    name[1] = int(name[1])
    names.append(name)
namesCopy = copy.deepcopy(names)


def findExtraFriend(centerScore: list, listOfNames: list):
    relCircle2 = RelationshipCircle(listOfNames, centerScore[1], barkadaSize)
    relCircle2.addDistance()
    relCircle2.sortByDistance()
    relCircle2.sortByScore()
    relCircle2.sortByName()
    relCircle2.addToBarkada()
    namesInBarkada = [x[0] for x in relCircle1.barkada]
    if relCircle2.barkada[1][2] == relCircle1.barkada[0][2]:
        if relCircle2.barkada[1][0] in namesInBarkada:
            print(centerScore[0])
        else:
            print("{}, {}".format(centerScore[0], relCircle2.barkada[1][0]))
    else:
        print("{}, {}".format(centerScore[0], "almost"))


relCircle1 = RelationshipCircle(names, score, barkadaSize)
relCircle1.addDistance()
relCircle1.sortByDistance()
relCircle1.sortByScore()
relCircle1.sortByName()
relCircle1.addToBarkada()


for i in relCircle1.barkada:
    print(i[0])
extraFriend = relCircle1.listOfNames[barkadaSize]
findExtraFriend(extraFriend, namesCopy)
