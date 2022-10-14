Valnums = [35, 26, 19, 23, 6, 8, 18, 1, 34]
numResult = []

numResult.append(Valnums[3])
numResult.append(Valnums[-1])
numResult.append(Valnums[:4])
numResult.append(Valnums[6:])
numResult.append(Valnums[2:5])
numResult.append(Valnums[3:7])
numResult.append(Valnums[1::2])
numResult.append(Valnums[::-1])

for x in numResult:
    print(x)
