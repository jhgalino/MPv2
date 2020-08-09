def unwrap(sandwich: str, se: set, wordLength: int) -> list:
    if len(sandwich) == wordLength:
        return [sandwich]
    wordComb = iterateCombinations(sandwich, se, wordLength)
    word = sandwich[: wordComb[0]] + sandwich[-wordComb[1] :]
    newSandwich = removeWord(sandwich, wordComb)
    return unwrap(newSandwich, se, wordLength) + [word]
    # get last wordlength - 1 characters
    # try to find a word inside letters
    # remove letters
    # return func + word


def iterateCombinations(sandwich: str, se: set, wordLength: int) -> list:
    combinations = [[x, (wordLength - x)] for x in range(1, wordLength)]
    for comb in combinations:
        tryWord = sandwich[: comb[0]] + sandwich[-comb[1] :]
        if tryWord in se:
            return comb


def removeWord(sandwich: str, comb: int) -> str:
    sandwich = list(sandwich)
    for n in range(comb[0]):
        sandwich.pop(0)
    for n in range(comb[1]):
        sandwich.pop()
    return "".join(sandwich)


# print(
#     unwrap(
#         "aloacrbbbpgsasjgsftactipewpyemawhygeinapanoyedaributidweidsh",
#         set(
#             [
#                 "bar",
#                 "rib",
#                 "act",
#                 "shy",
#                 "spy",
#                 "few",
#                 "gem",
#                 "owe",
#                 "pan",
#                 "aid",
#                 "lid",
#                 "gap",
#                 "age",
#                 "cut",
#                 "sin",
#                 "boy",
#                 "jaw",
#                 "bed",
#                 "tip",
#                 "ash",
#             ]
#         ),
#         3,
#     )
# )

# print(unwrap("brbacpattyonead", set(["bacon", "patty", "bread"]), 5))
OTHER_RECURSIVE_FUNCTIONS = ["iterateCombinations", "removeWord"]

