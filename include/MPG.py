from memory_profiler import profile

arrayOfSubArray = []
numberOfID = int(input())
ids = [int(x) for x in input().split()]


@profile
def func():
    highestValue = 0
    for n in range(2, numberOfID + 1):
        x = 0
        while x + n != numberOfID + 1:
            toSrt = ids[x : x + n]
            toSrt.sort()
            arrayOfSubArray.append(toSrt[:2])
            x += 1

    for x in arrayOfSubArray:
        currentValue = ((x[0] & x[1]) ^ (x[0] ^ x[1])) | (x[0] ^ x[1])
        if currentValue > highestValue:
            highestValue = int(currentValue)

    print(highestValue)


func()
