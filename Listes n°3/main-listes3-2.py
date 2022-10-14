ValNums = [31, 18, 25, 34, 23, 24, 40, 37, 4, 31]
ValNumsResult = []

ValNumsResult.append(ValNums[2])
ValNumsResult.append(ValNums[-1])
ValNumsResult.append(ValNums[:-1])
ValNumsResult.append(ValNums[3:])
ValNumsResult.append(ValNums[1:4])
ValNumsResult.append(ValNums[5:8])
ValNumsResult.append(ValNums[::2])
ValNumsResult.append(ValNums[::-1])

for x in ValNumsResult:
    print(x)