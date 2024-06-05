from utils.print_sheet import printSheet
import re

class Sheet:
    def __init__(self,sheetName):
        self.sheetName = sheetName
        self.sheetValue = [
                           [0,0,0],
                           [0,0,0],
                           [0,0,0]
                           ]
        
    def show_sheet(self):
        printSheet(self.sheetValue)
    
    def expression_handler(*args):
        
        
        args = args[1:]
        args =  ''.join(args)
        tokens = re.findall(r'\d+|\+|\-|\*|\/', args)
        exp = ['*','/']
        for x in exp:
          while(x in tokens) :
              idx = tokens.index(x)
              if x == "*":
                res = int(tokens[idx-1])*int(tokens[idx+1])
              else:
                res = int(tokens[idx-1])/int(tokens[idx+1])
              tokens.pop(idx-1)
              tokens.pop(idx)
              tokens[idx-1] =res

        result = int(tokens[0])
        for idx,arg in enumerate(tokens):
            if arg == '+':
                result += int(tokens[idx+1])
            elif arg =='-':
                result -= int(tokens[idx+1])
            
        return result
            
            
        
    
    def change_value(self,expression):
        row,col,val = expression.split(" ")
        col = int(col)
        row = int(row)
        if val.isdigit() == True:
            self.sheetValue[row][col] = int(val)
        else:
            self.sheetValue[row][col] = self.expression_handler(*val)
        
        self.show_sheet()