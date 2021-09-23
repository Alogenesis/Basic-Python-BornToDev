list1 = [0,2,4,6,8]
for i in list1:
    print(i)

customerList = ["Born","Dev","Winai"]
print(customerList[0])
print(customerList[:2])
print(customerList[1:2])
print("-"*20)
for i in customerList:
    print(i)
print("-"*20)

myFriends = ["Winai","Pang","Ton"]
print(myFriends)
myFriends.append("bank")
print(myFriends)
myFriends.remove("Ton")
print(myFriends)
myFriends[1] = "Pang Pond"
print(myFriends)
del myFriends[0]
print(myFriends)