from utils.menu import menu

from modules.user import user

def check_expression(expression, option):
    if option == 1:
        if " " in expression:
            print("wrong input format")
            return False
    elif option == 2:
        sheetName = expression.split(" ")
        if len(sheetName) != 2:
            print("wrong input format")
            return False
    return True

def run():
    users = {}
    while(True):
        menu()
        data = input("> ")
        if data == '0' :
            print("Exit program")
            break
        elif data == '1':
            userName = input("> ")
            if check_expression(userName, 1):
                users[userName] = user(userName)
        elif data == '2':
            sheetName = input("> ")
            if check_expression(sheetName, 2):
                userName,sheetName = sheetName.split(' ')
                if userName in users:
                    users[userName].create_sheet(sheetName)
                    print(f"Create a sheet named \"{sheetName} \" for \"{userName}\"")
                else:
                    print(f"User \"{userName}\" does not exist")
        elif data == '3':
            sheetName = input("> ")
            userName,sheetName = sheetName.split(' ')
            if userName in users:
                user1 = users[userName]
                if sheetName in user1.sheet:
                    sheet = user1.sheet[sheetName]
                    sheet.show_sheet()
                else:
                    print(f"Sorry, sheet \"{sheetName}\" does not exist")
            else:
                print(f"User \"{userName}\" does not exist")
        elif data == '4':
            sheetName = input("> ")
            userName,sheetName = sheetName.split(' ')
            if userName in users:
                user1 = users[userName]
                if sheetName in user1.sheet:
                    sheet = user1.sheet[sheetName]
                    sheetValue = input("> ")
                    sheet.change_value(sheetValue)
                else:
                    print(f"Sorry, sheet \"{sheetName}\" does not exist")
            else:
                print(f"User \"{userName}\" does not exist")
        else:
            print("Please enter a number")

            
            