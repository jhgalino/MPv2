def unwrap(sandwich: str, se: set, wordLength: int):
    wordStart, wordEnd = findInString(sandwich, se, wordLength)
    word = sandwich[wordStart:wordEnd]
    newSandwich = removeString(wordStart, wordEnd, sandwich)
    if len(newSandwich) == 0:
        toReturn = [word]
        assert type(toReturn) == list, "return"
        return toReturn
    else:
        toReturn = [word] + unwrap(newSandwich, se, wordLength)
        assert type(toReturn) == list, "return"
        return toReturn


def findInString(string: str, setOfWords: set, length: int):
    for element in setOfWords:
        if element in string:
            wordStart = string.index(element)
            wordEnd = string.index(element) + length
            return (wordStart, wordEnd)


def removeString(indexStart: int, indexEnd: int, stringSandwich: str):
    stringSandwich = stringSandwich[:indexStart] + stringSandwich[indexEnd:]
    return stringSandwich


OTHER_RECURSIVE_FUNCTIONS = ["findInString", "removeString"]
