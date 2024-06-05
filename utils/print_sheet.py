def printSheet(sheetValue):
    for idx,row in enumerate(sheetValue):
        # print(val,end=", ")
        # if (idx+1) % 3==0:
        # print(row)
        for col in row:
            print(col,end=", ")
        print()
        