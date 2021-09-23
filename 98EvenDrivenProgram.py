from tkinter import *

def leftClickButton(event):
    print("Left Click!!")

def rightClickButton(event):
    print("Right Click !!")

def doubleLeftClick(event):
    print("Double Left Click")

def doubleRightClick(event):
    print("Double Right Click")



main = Tk()
button = Button(main, text="My Button !!")
button.pack()
button.bind('<Button-1>',leftClickButton)
button.bind('<Button-3>',rightClickButton)
button.bind('<Double-1>',doubleLeftClick)
button.bind('<Double-3>',doubleRightClick)
main.mainloop()