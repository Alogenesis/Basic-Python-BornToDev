def login():
    userNameInput = input("Username : ")
    passwordInput = input("Password : ")
    if userNameInput == "admin" and passwordInput == "inmad":
        return True
    else:
        return False
def showMenu():
    print("Log in complete")
    print("iShop Menu")
    print("1. Vat Calculator")
    print("2. Plus Calculator")
def menuSelect():
    menuselected = int(input("Menu number : "))
    return
def vatCalculate():
    pass
def priceCalculate():
    pass

login()
userNameInput = input("Username : ")
passwordInput = input("Password : ")

if userNameInput == "admin" and passwordInput == "inmad":
    print("Log in complete")
    print("iShop Menu")
    print("1. Vat Calculator")
    print("2. Plus Calculator")
    menuselected = int(input("Menu number : "))
    if menuselected == 1:
        price = int(input("Price (THB) : "))
        vat = 7
        result = price + (price * vat / 100)
        print("Including vat cost is ", result)
    elif menuselected ==2:
        price1 = int(input("Price of menu 1 = ? "))
        price2 = int(input("Price of menu 2 = ? "))
        print("total cost is (THB) ")
    else:
        print("End Menu")
else:
    print("invalid Username or Password")

#Login
#Show Menu
#Select Menu
#Vat
#Price