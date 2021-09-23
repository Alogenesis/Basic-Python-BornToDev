from tkinter import *

def sayHelloWorld():
    print("HelloWorld")

mainWindow = Tk()
button = Button(mainWindow, text="Click me1", command = sayHelloWorld).grid(row=2,column=1)
button2 = Button(mainWindow, text="Click me2", command = sayHelloWorld).grid(row=1,column=1)
button3 = Button(mainWindow, text="Click me3", command = sayHelloWorld, fg = "red", bg = "blue").grid(row=0,column=2)
label = Label(mainWindow, text = "Hello World", width = 20, foreground = "red", background = "blue",font=("Helvetica",38),anchor=E).grid(row=0,column=1)
mainWindow.mainloop()