def unwrap(sandwich: str, se: set, wordLength: int):
    try:
        indexStart = findWord(sandwich, se)
    except Exception as e:
        print(e)
        raise SystemExit
    try:
        getWord = sandwich[indexStart : indexStart + wordLength]
    except Exception as e:
        print(indexStart, wordLength)
        raise SystemExit
    try:
        newSandwich = removeWord(sandwich, indexStart, indexStart + wordLength)
    except Exception as e:
        print(e)
        raise SystemExit
    if len(newSandwich) == 0:
        return [getWord]
    else:
        return [getWord] + unwrap(newSandwich, se, wordLength)


def findWord(wordSandwich: str, setOfWords: set) -> int:
    for word in setOfWords:
        if word in wordSandwich:
            indexStart = wordSandwich.find(word)
            if word == "rib":
                print(wordSandwich[indexStart - 3 : indexStart + 8])
            assert indexStart != -1
            return indexStart
    return "not in Word"


def removeWord(wordSandwich: str, indexStart: int, indexEnd: int) -> str:
    wordSandwich = list(wordSandwich)
    wordSandwich = wordSandwich[:indexStart] + wordSandwich[indexEnd:]
    wordSandwich = "".join(wordSandwich)
    return wordSandwich


# print(unwrap("stappleyle", set(["style", "apple"]), 5))

OTHER_RECURSIVE_FUNCTIONS = ["findWord", "removeWord"]

