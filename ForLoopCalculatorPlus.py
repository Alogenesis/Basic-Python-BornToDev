inputRound = int(input("How many round you need? : "))
sum = 0
for x in range(inputRound):
    inputNumber = int(input("x"+str(x+1)+":"))
    sum += inputNumber
print("total", sum)