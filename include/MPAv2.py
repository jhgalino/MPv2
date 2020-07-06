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
        print(self.listOfNames)

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
        print(self.listOfNames)

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
        print(self.listOfNames)

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

relCircle1 = RelationshipCircle(names, score, barkadaSize)
relCircle1.addDistance()
relCircle1.sortByDistance()
relCircle1.sortByScore()
relCircle1.sortByName()
relCircle1.addToBarkada()


extra = relCircle1.listOfNames[barkadaSize]
for i in relCircle1.barkada:
    print(i[0])
