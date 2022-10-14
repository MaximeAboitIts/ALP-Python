ValNums = [11, 29, 22, 36, 40, 25, 14, 7, 16]
ValNumsResult = []

ValNumsResult.append(ValNums[1:2:])
ValNumsResult.append(ValNums[6:9:])
ValNumsResult.append(ValNums[3:7])
ValNumsResult.append(ValNums[-1:-6:-1])

for x in ValNumsResult:
    print(x)