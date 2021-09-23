from tkinter import *

def sayHelloWorld():
    print("HelloWorld")

mainWindow = Tk()
button = Button(mainWindow, text="Click me1", command = sayHelloWorld).grid(row=0,column=1)
button2 = Button(mainWindow, text="Click me2", command = sayHelloWorld).grid(row=1,column=1)
button3 = Button(mainWindow, text="Click me3", command = sayHelloWorld).grid(row=0,column=2)
mainWindow.mainloop()