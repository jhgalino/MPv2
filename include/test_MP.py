def unwrap(sandwich: str, se: set, wordLength: int):
    assert type(sandwich) == str, "type(sandwich) == str"
    assert type(se) == set, "type(se) == set"
    assert type(wordLength) == int, "type(wordLength) == int"
    try:
        wordStart, wordEnd = findInString(sandwich, se, wordLength)
    except Exception:
        print("error: findInString")
    word = sandwich[wordStart:wordEnd]
    assert word in se, "word in se"
    sandwich = removeString(wordStart, wordEnd, sandwich)
    if len(sandwich) == 0:
        return [word]
    else:
        return [word] + unwrap(sandwich, se, wordLength)


def findInString(string: str, setOfWords: set, length: int):
    for n in range((len(string) - length) + 1):
        for m in range(length - 1, len(string) - 1):
            tempWord = string[n:m]
            if tempWord in setOfWords:
                return n, m


def removeString(indexStart: int, indexEnd: int, stringSandwich: str):
    assert type(indexStart) == int, "type(indexStart) == int"
    assert type(indexEnd) == int, "type(indexEnd) == int"
    stringSandwich = stringSandwich[:indexStart] + stringSandwich[indexEnd:]
    assert type(stringSandwich) == str, "assert type(stringSandwich) == str"
    return stringSandwich


def test_func_01():
    assert unwrap("brbacpattyonead", set(["bacon", "patty", "bread"]), 5) == [
        "patty",
        "bacon",
        "bread",
    ]
    assert unwrap("stappleyle", set(["style", "apple"]), 5) == ["apple", "style"]

