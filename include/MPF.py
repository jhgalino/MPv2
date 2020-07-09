def findTroll(stack: list):
    if len(stack) == 0 or noMoreTrolls(stack):
        return "Goodbye trolls!"
    else:
        backs = -1
        possibleTroll = stack[0]
        for element in stack:
            backs += 1
            if element[-1] < possibleTroll[-1]:
                possibleTroll = element
                for n in range(backs):
                    possibleTroll.insert(0, "<")
        return possibleTroll


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
        troll = findTroll(executionStack)
        if type(troll) != str:
            executionStack = deleteFromStack(troll, executionStack)
        if type(troll) != str:
            print(" ".join(troll[:-1]))
        else:
            print(troll)
    else:
        command[1] = int(command[1])
        executionStack.insert(0, command)

