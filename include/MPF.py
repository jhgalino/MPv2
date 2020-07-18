def insertBacks(stackToScan: list, leastFriends: list):
    index = stackToScan.index(leastFriends)
    for n in range(index):
        leastFriends.insert(0, "<")
    return leastFriends


def findLeastScore(listToSearch: list):
    if len(listToSearch) > 0 and noMoreTrolls(listToSearch) is False:
        return min(listToSearch, key=lambda x: x[-1])
    else:
        return "Goodbye trolls!"


def noMoreTrolls(stackToScan: list):
    for element in stackToScan:
        if element[-1] <= 50:
            return False
    return True


def deleteFromStack(trollToFind: list, stack: list):
    indexOfTroll = stack.index(trollToFind)
    stack.pop(indexOfTroll)
    return stack


commandQueue = []
executionStack = []
numberOfInputs = int(input())

for n in range(numberOfInputs):
    command = [x for x in input().split()]
    commandQueue.append(command)

for command in commandQueue:
    if "report" in command:
        troll = findLeastScore(executionStack)
        if type(troll) == str:
            print(troll)
        else:
            troll = insertBacks(executionStack, troll)
            print(" ".join(troll[:-1]))
            executionStack = deleteFromStack(troll, executionStack)
    else:
        command[1] = int(command[1])
        executionStack.insert(0, command)

