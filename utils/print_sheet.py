def printSheet(sheetValue):
    for idx,val in enumerate(sheetValue):
        print(val,end=", ")
        if (idx+1) % 3==0:
            print()
            