setTest = {'apple','banana','orange'}
for x in setTest:
    print(x)
print('apple' in setTest)
print("-"*20)
fruit = {'apple','banana','orange','pineapple'}
print(fruit)
fruit.remove('banana')
print(fruit)
fruit.clear()
print(fruit)
fruit.add("grape")
print(fruit)
print("-"*20)

userInput = int(input("Enter number of your favorite fruits >>"))
myFruits = set()
while (len(myFruits)<userInput):
    myFruits.add(input("Fruits : "))
    print(myFruits)










