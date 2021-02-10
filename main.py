import tkinter 
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""

def btn1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn0_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_Plus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_Minus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)
    
def btn_Mul_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "x"
    val = val + "x"
    data.set(val)

def btn_Div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def clear():
    global A
    global operator
    global val

    val = ""
    A = 0
    operator = ""
    data.set(val)

def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val = str(c)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val = str(c)
    elif operator == "x":
        x = int((val2.split("x")[1]))
        c = A * x
        data.set(c)
        val = str(c)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error","BOSS SOMETHING IS WRONG")
            A = ""
            val = ""
            data.set(val)
        else:
            c = A / x
            data.set(c)
            val = str(c)
    
root=tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

data = StringVar()
Lbl = Label(root, text="Label", anchor=SE, font=("Verdana", 20), textvariable = data, background = "#ffffff", fg="#000000")
Lbl.pack(expand=True, fill="both")

btnrow1 = Frame(root,)
btnrow1.pack(expand=True,fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

#Button row 1

btn1 = Button(btnrow1, text="1", font=("Verdana", 22), relief=GROOVE, border=0, command = btn1_isclicked)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(btnrow1, text="2", font=("Verdana", 22), relief=GROOVE, border=0, command = btn2_isclicked)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(btnrow1, text="3", font=("Verdana", 22), relief=GROOVE, border=0, command = btn3_isclicked)
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(btnrow1, text="+", font=("Verdana", 22), relief=GROOVE, border=0, command = btn_Plus_clicked)
btn4.pack(side=LEFT, expand=True, fill="both")

#Button row 2
btn1 = Button(btnrow2, text="4", font=("Verdana", 22), relief=GROOVE, border=0, command = btn4_isclicked)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(btnrow2, text="5", font=("Verdana", 22), relief=GROOVE, border=0, command = btn5_isclicked)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(btnrow2, text="6", font=("Verdana", 22), relief=GROOVE, border=0, command = btn6_isclicked)
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(btnrow2, text="-", font=("Verdana", 22), relief=GROOVE, border=0, command = btn_Minus_clicked)
btn4.pack(side=LEFT, expand=True, fill="both")

#Button row 3
btn1 = Button(btnrow3, text="7", font=("Verdana", 22), relief=GROOVE, border=0, command = btn7_isclicked)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(btnrow3, text="8", font=("Verdana", 22), relief=GROOVE, border=0, command = btn8_isclicked)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(btnrow3, text="9", font=("Verdana", 22), relief=GROOVE, border=0, command = btn9_isclicked)
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(btnrow3, text="x", font=("Verdana", 22), relief=GROOVE, border=0, command = btn_Mul_clicked)
btn4.pack(side=LEFT, expand=True, fill="both")

#Button row 4
btn1 = Button(btnrow4, text="C", font=("Verdana", 22), relief=GROOVE, border=0, command = clear)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(btnrow4, text="0", font=("Verdana", 22), relief=GROOVE, border=0, command = btn0_isclicked)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(btnrow4, text="=", font=("Verdana", 22), relief=GROOVE, border=0, command = result)
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(btnrow4, text="/", font=("Verdana", 22), relief=GROOVE, border=0, command = btn_Div_clicked)
btn4.pack(side=LEFT, expand=True, fill="both")

root.mainloop()
