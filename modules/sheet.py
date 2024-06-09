from utils.print_sheet import printSheet
import re

def check_access(func):
    def wrapper(self, *args, **kwargs):
        if self.current_access == 'read-only':
            print("This sheet is not accessible.")
            return
        return func(self, *args, **kwargs)
    return wrapper

def collaborate_checker(userName,sheetName,userList):
    for user in userList.values():
        if sheetName in user.sheet.keys():
            sheet = user.sheet[sheetName]
            if sheet != None:
                if userName in sheet.access['read-only'] or userName in sheet.access['editable'] or userName == sheet.owner:
                    return sheet
                else:
                    return "no_access"
            else:
                return "no_sheet_found"
            
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

class Sheet:
    def __init__(self,sheetName,name):
        self.sheetName = sheetName
        self.sheetValue = [
                           [0,0,0],
                           [0,0,0],
                           [0,0,0]
                           ]
        self.access = {'read-only':[],
                       'editable':[]}
        self.current_access = 'editable'
        self.owner = name
        

        
    def show_sheet(self):
        printSheet(self.sheetValue)
    
    @check_access
    def change_value(self,expression):
        row,col,val = expression.split(" ")
        col = int(col)
        row = int(row)
        if row >2 or row <0 or col>2 or col<0:
            print("Invalid input please put in the range of 0 to 2")
        elif val.isdigit() == True:
            self.sheetValue[row][col] = int(val)
        else:
            self.sheetValue[row][col] = self.expression_handler(*val)
        
        self.show_sheet()

    def change_access(self,expression,name):
        # if name != self.owner:
        #     print("Sorry you are not the owner the sheet, please contact the owner to change the permission")
        #     return 
        expression = expression.lower()
        possible_read_access = ['read','readonly','read-only',]
        possible_write_access = ['write','edit','editable']
        if name != self.owner:
            if (name not in self.access['read-only'] or name not in self.access['editable'] ):
                print("Sorry you have not been added into the collaboration,please contact the owner to add you ")
                return
            if expression in possible_read_access:
                if name in access['editable']:
                    self.access['editable'].remove(name)
                self.access['read-only'].append(name)
            elif expression in possible_write_access:
                if name in access['read-only']:
                    self.access['read-only'].remove(name)
                self.access['editable'].append(name)
        else:
            
            if expression in possible_read_access:
                self.current_access = 'read-only'
            else:
                self.current_access = 'editable'
    
    def grant_access(self,name):
        if self.current_access == 'read-only':
            self.access['read-only'].append(name)
        elif self.current_access == 'editable':
            self.access['editable'].append(name)
        print(f"Share \"{self.owner}\"'s \"{self.sheetName}\" with \"{name}\".")

        
            