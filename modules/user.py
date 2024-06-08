from modules.sheet import Sheet

class user:
    def __init__(self,userName):
        self.userName = userName
        self.sheet = {}
        print("Create a user named \""+userName+"\"")
    def create_sheet(self,sheetName,name):
        self.sheet[sheetName] = Sheet(sheetName,name)
        
    