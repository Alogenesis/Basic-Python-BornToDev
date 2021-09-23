text = "Hello"
print(text[0:4])
print(text[1])

address = "642/17 Sukhumvit Bangkok"
print("Sukhumvit" not in address)

name = "Winai"
weight = "74"
print("Hello " + name +"! and weight is "+ weight + " kg")
print("Hello %s!, Age are %d and weight are %f kg" %(name,28,74.5256))
""" %s = string
    %d = decimal integer
    %f = float
"""
fName = input("First name >>").capitalize()
lName = input("Last name >>").capitalize()
print("Welcome %s %s" %(fName.capitalize(),lName))

text = "Winai"
textFormatted = "Welcome %s" %(text)
print(textFormatted.center(21,"-"))
print(len(name)) '''len for count character in string'''
