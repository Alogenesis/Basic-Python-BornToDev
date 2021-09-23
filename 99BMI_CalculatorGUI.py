from tkinter import *
import math

def leftClickButton(event):
    bmi = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(bmi)
    labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))


def rightClickButton(event):
    print("Right Click !!")



main = Tk()
labelHeight = Label(main,text = "ส่วนสูง (CM.)")
labelHeight.grid(row=0, column=0)
textBoxHeight = Entry(main)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(main,text = "น้ำหนัก (Kg.)")
labelWeight.grid(row=1, column=0)
textBoxWeight = Entry(main)
textBoxWeight.grid(row=1, column=1)
calculateButton = Button(main, text = "คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2, column=0)
labelResult = Label(main,text = "ผลลัพธ์")
labelResult.grid(row=2, column=1)
main.mainloop()