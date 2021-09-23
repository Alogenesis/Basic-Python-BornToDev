print("Please Log in")
userNameInput = input("Username : ")
passwordInput = input("Password : ")

if (userNameInput == "admin") and (passwordInput == "admin"):
    print("Log in successful")
else:
    print("invalid ID or Password")

