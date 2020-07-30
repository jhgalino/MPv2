numberOfID = int(input())
ids = list(map(int, input().split()))
highestValue = 0
arrayOfSubArray = [
    tuple(ids[i : i + j])
    for i in range(numberOfID - 1)
    for j in range(2, numberOfID + 1)
]
setOfSubArray = list(map(list, set(arrayOfSubArray)))

for x in arrayOfSubArray:
    first = x[0]
    second = x[1]
    currentValue = ((first & second) ^ (first ^ second)) | (first ^ second)
    if currentValue > highestValue:
        highestValue = int(currentValue)

print(highestValue)
