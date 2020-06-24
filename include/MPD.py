def top_and_bottom(li: list, n: int):
    sortedList = []
    while True:
        if len(li) >= n:
            for number in range(n):
                if type(li[0]) == list:
                    li[0] = top_and_bottom(li[0], n)
                    sortedList.append(li[0])
                    li.pop(0)
                else:
                    sortedList.append(li[0])
                    li.pop(0)
        else:
            for element in li:
                sortedList.append(li[0])
                li.pop(0)
            break

        if len(li) >= n:
            for number in range(n):
                if type(li[-1]) == list:
                    li[-1] = top_and_bottom(li[-1], n)
                    sortedList.append(li[-1])
                    li.pop(-1)
                else:
                    sortedList.append(li[-1])
                    li.pop(-1)
        else:
            for element in li:
                sortedList.append(li[-1])
                li.pop(-1)
            break

    return sortedList


print(top_and_bottom([1, 2, 3, 4, 5, 6, 7], 2))
