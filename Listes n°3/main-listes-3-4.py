from logging.config import valid_ident


ValNums = [2, 4, 6]
ValNumsResult = []

ValNums.append(ValNums[3])
ValNums.append(ValNums[-3])

for x in ValNumsResult:
    print(x)