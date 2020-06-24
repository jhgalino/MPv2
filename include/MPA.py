class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
        return other.obj < self.obj


# processing
def process(personalScore):
    tempStorage = list(
        map(lambda x: [x[0], x[1], abs(personalScore - int(x[1]))], storage)
    )
    tempStorage = sorted(
        tempStorage, key=lambda x: (x[2], x[1], len(x[0]), reversor(x[0]))
    )
    return tempStorage


def extra(
    scoreGap, barkada: list
):  # scoreGap is the gap between your score and your closest
    extraPerson = storage[barkadaSize]
    modifiedStorage = process(int(extraPerson[1]))
    personWithCloseness = list(filter(lambda x: x[2] == scoreGap, modifiedStorage))
    personWithCloseness = sorted(
        personWithCloseness, key=lambda x: (x[2], x[1], len(x[0]), reversor(x[0]))
    )
    if len(personWithCloseness) == 0:
        return "{}, almost".format(extraPerson[0])
    else:
        if personWithCloseness[0][0] in barkada:
            return extraPerson[0]
        else:
            return "{}, {}".format(extraPerson[0], personWithCloseness[0][0])


# input
storage = []
personalScore = int(input())
barkadaSize = int(input())
numberOfNamesToFollow = int(input())
for n in range(numberOfNamesToFollow):
    name, score = [str(x) for x in input().split()]
    storage.append([name, score])

storage = process(personalScore)
barkada = [storage[number][0] for number in range(barkadaSize)]
lastLine = extra(storage[0][2], barkada)

# output
for i in barkada:
    print(i)
print(lastLine)
