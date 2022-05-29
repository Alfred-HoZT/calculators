# program gives a simple calculator with gui

import math
from tkinter import *

from mysqlx import Column
from numpy import subtract

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=16, font=('bold', 20), borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "Enter your name: ")
global math
math = 0

def button_click(number):
    if math == "equal":
        e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    global math
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))
    
    math = "equal"

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)

# Define Buttons 

button_1 = Button(root, text="1", font=("bold", 15), padx=30, pady=10, command=lambda: button_click(1))
button_2 = Button(root, text="2", font=("bold", 15), padx=30, pady=10, command=lambda: button_click(2))
button_3 = Button(root, text="3", font=("bold", 15), padx=30, pady=10, command=lambda: button_click(3))
button_4 = Button(root, text="4", font=("bold", 15), padx=30, pady=10, command=lambda: button_click(4))
button_5 = Button(root, text="5", font=("bold", 15), padx=30, pady=10, command=lambda: button_click(5))
button_6 = Button(root, text="6", font=("bold", 15), padx=30, pady=10, command=lambda: button_click(6))
button_7 = Button(root, text="7", font=("bold", 15), padx=30, pady=10, command=lambda: button_click(7))
button_8 = Button(root, text="8", font=("bold", 15), padx=30, pady=10, command=lambda: button_click(8))
button_9 = Button(root, text="9", font=("bold", 15), padx=30, pady=10, command=lambda: button_click(9))
button_0 = Button(root, text="0", font=("bold", 15), padx=30, pady=10, command=lambda: button_click(0))
button_add = Button(root, text="+", font=("bold", 15), padx=29, pady=10, command=button_add)
button_equal = Button(root, text="=", font=("bold", 15), padx=74, pady=10, command=button_equal)
button_clear = Button(root, text="Clear", font=("bold", 13), padx=62, pady=10, command=button_clear)

button_subtract = Button(root, text="-", font=("bold", 15), padx=32, pady=10, command=button_subtract)
button_multiply = Button(root, text="x", font=("bold", 15), padx=31, pady=10, command=button_multiply)
button_divide = Button(root, text="/", font=("bold", 15), padx=32, pady=10, command=button_divide)

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
