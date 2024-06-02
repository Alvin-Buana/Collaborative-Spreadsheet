from utils.print_sheet import printSheet

class Sheet:
    def __init__(self,sheetName):
        self.sheetName = sheetName
        self.sheetValue = [0,0,0,
                           0,0,0,
                           0,0,0]
        
    def show_sheet(self):
        printSheet(self.sheetValue)