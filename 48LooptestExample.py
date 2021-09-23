number1 = int(input("Number1 : "))
for x in range(number1):
    text = ""
    for y in range(x+1):
        text += "*"
    print(text)
