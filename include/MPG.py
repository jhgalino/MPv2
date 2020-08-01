numberOfID = int(input())
ids = list(map(int, input().split()))
highestValue = 0
arrayOfSubArray = [ids[i : i + 2] for i in range(numberOfID - 1)]

for x in arrayOfSubArray:
    first = x[0]
    second = x[1]
    currentValue = ((first & second) ^ (first ^ second)) | (first ^ second)
    if currentValue > highestValue:
        highestValue = int(currentValue)

print(highestValue)
