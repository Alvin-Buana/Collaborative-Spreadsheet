from utils.menu import menu

from modules.user import user
from modules.sheet import collaborate_checker

def check_expression(expression, option, userList = []):
    if option == 1:
        if " " in expression:
            print("wrong input format")
            return False
    elif option == 2:
        sheetName = expression.split(" ")
        if len(sheetName) != 2:
            print("wrong input format")
            return False
    elif option == 3:
        sheetName = expression.split(" ")
        if len(sheetName) != 3:
            print("wrong input format")
            return False
    elif option == 4:
        for user in userList:
            if expression in user.sheet:
                sheet = user.sheet[expression]
                if expression in sheet.access['read-only'] or expression in sheet.access['editable']:
                    return sheet
    return True
        
def run():
    userList = {}
    sheetList = []
    while(True):
        menu()
        data = input("> ")
        if data == '0' :
            print("Exit program")
            break
        elif data == '1':
            userName = input("> ")
            if check_expression(userName, 1):
                userList[userName] = user(userName)
        elif data == '2':
            sheetName = input("> ")
            if check_expression(sheetName, 2):
                if sheetName in sheetList:
                    print("Sheet name already exist")
                else:
                    userName,sheetName = sheetName.split(' ')
                    if userName in userList:
                        userList[userName].create_sheet(sheetName,userName)
                        sheetList.append(sheetName)
                        print(f"Create a sheet named \"{sheetName} \" for \"{userName}\"")
                    else:
                        print(f"User \"{userName}\" does not exist")
        elif data == '3':
            sheetName = input("> ")
            if check_expression(sheetName, 2):
                userName,sheetName = sheetName.split(' ')
                if userName in userList:
                    user1 = userList[userName]
                    if sheetName in user1.sheet:
                        sheet = user1.sheet[sheetName]
                        sheet.show_sheet()
                    else:
                        print(f"Sorry, sheet \"{sheetName}\" does not exist")
                else:
                    print(f"User \"{userName}\" does not exist")
        elif data == '4':
            sheetName = input("> ")
            if check_expression(sheetName, 2):
                userName,sheetName = sheetName.split(' ')
                if userName in userList:
                    user1 = userList[userName]
                    sheet = collaborate_checker(userName,sheetName,userList)
                    if sheet == "no_access":
                        print(f"User \"{userName} doesn't have access to the sheet")
                    elif sheet == "no_sheet_found" or sheet == None:
                        print(f"sheet doesn't exist")
                    else:
                        sheet.show_sheet()
                        sheetValue = input("> ")
                        if check_expression(sheetValue, 3):
                            sheet.change_value(sheetValue)
                else:
                    print(f"User \"{userName}\" does not exist")
        elif data == '5':
            sheetName = input("> ")
            if check_expression(sheetName, 3):
                userName,sheetName,permission = sheetName.split(' ')
                if userName in userList:
                    user1 = userList[userName]
                    sheet = collaborate_checker(userName,sheetName,userList)
                    if sheet == "no_access":
                        print(f"User \"{userName} doesn't have access to the sheet")
                    elif sheet == "no_sheet_found" or sheet == None:
                        print(f"sheet doesn't exist")
                    else:
                        user1.sheet[sheetName].change_access(expression = permission,name=userName)
                else:
                    print(f"User \"{userName}\" does not exist")
        elif data == '6':
            sheetName = input("> ")
            if check_expression(sheetName, 3):
                userName,sheetName,sharedPerson = sheetName.split(' ')
                if userName in userList:
                    user1 = userList[userName]
                    if sheetName in user1.sheet:
                        if sharedPerson in userList :
                            user1.sheet[sheetName].grant_access(name=sharedPerson)
                        else:
                            print(f"User \"{userName}\" does not exist")
                    else:
                        print(f"Sorry, sheet \"{sheetName}\" does not exist")
                else:
                    print(f"User \"{userName}\" does not exist")
        else:
            print("Please enter a number")

            
            