arrayOfSubArray = []
numberOfID = int(input())
ids = list(map(int, input().split()))


for n in range(2, numberOfID + 1):
    x = 0
    while x + n != numberOfID + 1:
        arrayOfSubArray.append(sorted(ids[x : x + n])[:2])
        x += 1

values = sorted(
    list(
        map(lambda x: ((x[0] & x[1]) ^ (x[0] ^ x[1])) | (x[0] ^ x[1]), arrayOfSubArray)
    )
)
print(values[-1])
