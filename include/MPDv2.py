def top_and_bottom(li: list, n: int):
    newDeck = []
    if len(li) == 0:
        return []
    else:
        for i in range(n):
            if len(li) != 0:
                tempHolder = li.pop(0)
                if type(tempHolder) is list:
                    tempHolder = top_and_bottom(tempHolder, n)
                    newDeck.append(tempHolder)
                else:
                    newDeck.append(tempHolder)
        for i in range(n):
            if len(li) != 0:
                tempHolder = li.pop()
                if type(tempHolder) is list:
                    tempHolder = top_and_bottom(tempHolder, n)
                    newDeck.append(tempHolder)
                else:
                    newDeck.append(tempHolder)
        newDeck.extend(top_and_bottom(li, n))
        return newDeck


print(top_and_bottom([1, [2, [3, 4], 5], [6, [7, [8, 9], 10]]], 1))
