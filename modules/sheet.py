from utils.print_sheet import printSheet

class Sheet:
    def __init__(self,sheetName):
        self.sheetName = sheetName
        self.sheetValue = [[0,0,0],
                           [0,0,0],
                           [0,0,0]
                           ]
        
    def show_sheet(self):
        printSheet(self.sheetValue)
    
    def change_value(self,expression):
        row,col,val = expression.split(" ")
        col = int(col)
        row = int(row)
        self.sheetValue[row][col] = int(val)
        self.show_sheet()