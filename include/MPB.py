# process
def filterCommonName(listOfNames: list, expectedNames: int):
    listOfUnique = []
    for name in listOfNames:
        if listOfNames.count(name) == 1:
            listOfUnique.append(name)
        if len(listOfUnique) == expectedNames:
            break
    if len(listOfUnique) < expectedNames:
        listOfUnique.append("Rumpelstiltskin")
    return listOfUnique


# input
listOfNames = []
expectedNames = int(input())
numberOfNames = int(input())
for n in range(numberOfNames):
    listOfNames.append(input())

listOfUnique = filterCommonName(listOfNames, expectedNames)

# output
for name in listOfUnique:
    print(name)
