Valnums = [7, 4, 27, 26, 2, 38, 19, 10, 34]
numResult = []

numResult.append(Valnums[5])
numResult.append(Valnums[0:1:])
numResult.append(Valnums[4:7:])
numResult.append(Valnums[1::2])

for x in numResult:
    print(x)