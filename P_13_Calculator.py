# Import all necessary libraries
from distutils.cmd import Command
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import font as tkFont
import math

# Initialize tkinter and set the display
root = tk.Tk()
root.configure(bg = "green")
root.title("Calculator MIN 3000")
root.geometry("294x389")
root.resizable(False, False)
options = {"padx": 1, "pady": 1}
relation = ""


#Function to update entered number and syntax in entry box
def button_click(num):
    """This function collects all the selected characters and displays them"""
    global relation
    relation = relation + str(num)
    equation.set(relation)


#Function to evaluate the final expresion
def click_equal():
    """This function evaluates the expression when equal is selected"""
    try:
        global relation
        total = str(eval(relation))
        equation.set(total)
        relation = ""

    except:
        equation.set("error")
        relation = ""


#Function to clear and delete the contents of text entry box
def delete():
    """This function deletes contents of text entry box"""
    global relation
    relation = ""
    equation.set("")
  

# Define variables and constants
equation = StringVar()
helv36 = tkFont.Font(family='Helvetica', size=20, weight=tkFont.BOLD)
sqrt = math.sqrt
prct = 1/100

# Configuration of the display and buttons
result_display = ttk.Entry(
    root, 
    textvariable = equation ,
    width=19,
    font=helv36
    ).grid(
        column=0, 
        row=0, 
        columnspan=4,  
        **options
        )

button_percent = Button(
    root, 
    text="%",
    width=3, 
    font=helv36, 
    bg="#ADD8E6", 
    command= lambda: button_click("prct")
    ).grid(
        column=0, 
        row=1, 
        sticky="nsew", 
        **options
        )

button_left_parenthesis = Button(
    root, 
    text="(", 
    width=3,
    command=lambda: button_click("("),
    font=helv36, 
    bg="#ADD8E6"
    ).grid(
        column=1, 
        row=1, 
        sticky="nsew", 
        **options
        )

button_right_parenthesis = Button(
    root, 
    text=")", 
    width=3,
    command=lambda: button_click(")"),
    font=helv36, 
    bg="#ADD8E6"
    ).grid(
        column=2, 
        row=1, 
        sticky="nsew", 
        **options
        )

button_del = Button(
    root, 
    text="DEL", 
    width=3, 
    font=helv36, 
    command = delete, 
    bg="#ADD8E6", 
    fg="red"
    ).grid(
        column=3, 
        row=1, 
        sticky="nsew", 
        **options
        )

button_square = Button(
    root, 
    text="x^2", 
    width=3,
    command=lambda: button_click("**2"),
    font=helv36, 
    bg="#ADD8E6"
    ).grid(
        column=0, 
        row=2, 
        sticky="nsew", 
        **options
        )

button_sqrt = Button(
    root, 
    text="√", 
    width=3,
    font=helv36, 
    bg="#ADD8E6", 
    command=lambda: button_click("sqrt")
    ).grid(
        column=1, 
        row=2, 
        sticky="nsew", 
        **options
        )

button_1_devide_x = Button(
    root, 
    text="1⁄x", 
    width=3,
    font=helv36, 
    bg="#ADD8E6"
    ).grid(
        column=2, 
        row=2, 
        sticky="nsew", 
        **options
        )

button_multiply = Button(
    root, 
    text="×", 
    width=3, 
    command= lambda: button_click("*"),
    font=helv36, 
    bg="#ADD8E6"
    ).grid(
        column=3, 
        row=2, 
        sticky="nsew", 
        **options
        )

button_7 = Button(
    root, 
    text="7", 
    width=3, 
    command=lambda: button_click(7),
    font=helv36
    ).grid(
        column=0, 
        row=3, 
        sticky="nsew", 
        **options
        )

button_8 = Button(
    root, 
    text="8", 
    width=3, 
    command=lambda: button_click(8),
    font=helv36
    ).grid(
        column=1, 
        row=3, 
        sticky="nsew", 
        **options
        )

button_9 = Button(
    root, 
    text="9", 
    width=3, 
    command=lambda: button_click(9),
    font=helv36
    ).grid(
        column=2, 
        row=3, 
        sticky="nsew", 
        **options
        )

button_devide = Button(
    root, 
    text="÷", 
    width=3, 
    command=lambda: button_click("/"),
    font=helv36, 
    bg="#ADD8E6"
    ).grid(
        column=3, 
        row=3, 
        sticky="nsew", 
        **options
        )

button_4 = Button(
    root, 
    text="4", 
    width=3, 
    command=lambda: button_click(4),
    font=helv36
    ).grid(
        column=0, 
        row=4, 
        sticky="nsew", 
        **options
        )

button_5 = Button(
    root, 
    text="5", 
    width=3, 
    command=lambda: button_click(5),
    font=helv36
    ).grid(
        column=1, 
        row=4, 
        sticky="nsew", 
        **options
        )

button_6 = Button(
    root, 
    text="6", 
    width=3, 
    command=lambda: button_click(6),
    font=helv36
    ).grid(
        column=2, 
        row=4, 
        sticky="nsew", 
        **options
        )

button_subtract = Button(
    root, 
    text="-", 
    width=3, 
    command=lambda: button_click("-"),
    font=helv36, 
    bg="#ADD8E6"
    ).grid(
        column=3, 
        row=4, 
        sticky="nsew", 
        **options
        )

button_1 = Button(
    root, 
    text="1", 
    width=3, 
    command=lambda: button_click(1),
    font=helv36
    ).grid(
        column=0, 
        row=5, 
        sticky="nsew", 
        **options
        )

button_2 = Button(
    root, 
    text="2", 
    width=3, 
    command=lambda: button_click(2),
    font=helv36
    ).grid(
        column=1, 
        row=5, 
        sticky="nsew", 
        **options
        )

button_3 = Button(
    root, 
    text="3", 
    width=3, 
    command=lambda: button_click(3),
    font=helv36
    ).grid(
        column=2, 
        row=5, 
        sticky="nsew", 
        **options
        )

button_add = Button(
    root, 
    text="+", 
    width=3, 
    command=lambda: button_click("+"),
    font=helv36, 
    bg="#ADD8E6"
    ).grid(
        column=3, 
        row=5, 
        sticky="nsew", 
        **options
        )

button_0 = Button(
    root, 
    text="0", 
    width=6, 
    command=lambda: button_click(0),
    font=helv36
    ).grid(
        column=0, 
        row=6, 
        columnspan=2, 
        sticky="nsew", 
        **options
        )

button_dot = Button(
    root, 
    text="∙", 
    width=3, 
    command=lambda: button_click("."),
    font=helv36
    ).grid(
        column=2, 
        row=6, 
        sticky="nsew", 
        **options
        )

button_equal = Button(
    root, 
    text="=", 
    width=3,
    command = click_equal, 
    font=helv36, 
    bg="#ADD8E6"
    ).grid(
        column=3, 
        row=6, 
        sticky="nsew", 
        **options
        )
    
root.mainloop()
