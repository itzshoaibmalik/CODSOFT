import tkinter as tk
from math import sqrt

def button_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")


def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)


def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""


def square_root():
    global expression
    try:
        result = str(sqrt(float(expression)))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""


root = tk.Tk()
root.title("Simple Calculator")


expression = ""
input_text = tk.StringVar()


input_frame = tk.Frame(root, bd=10, relief=tk.RIDGE)
input_frame.pack(pady=20)


input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=14, justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


btns_frame = tk.Frame(root)
btns_frame.pack()


num_color = "#ffffff"
op_color = "#ffeb3b"
sp_color = "#f44336"



# First row
clear_btn = tk.Button(btns_frame, text='C', fg='black', bg=sp_color, width=5, height=2, command=clear)
sqrt_btn = tk.Button(btns_frame, text='√', fg='black', bg=op_color, width=5, height=2, command=square_root)
divide_btn = tk.Button(btns_frame, text='/', fg='black', bg=op_color, width=5, height=2, command=lambda: button_click('/'))
backspace_btn = tk.Button(btns_frame, text='<--', fg='black', bg=sp_color, width=5, height=2, command=backspace)

clear_btn.grid(row=1, column=0, padx=5, pady=5)
sqrt_btn.grid(row=1, column=1, padx=5, pady=5)
divide_btn.grid(row=1, column=2, padx=5, pady=5)
backspace_btn.grid(row=1, column=3, padx=5, pady=5)

# Second row
seven_btn = tk.Button(btns_frame, text='7', fg='black', bg=num_color, width=5, height=2, command=lambda: button_click('7'))
eight_btn = tk.Button(btns_frame, text='8', fg='black', bg=num_color, width=5, height=2, command=lambda: button_click('8'))
nine_btn = tk.Button(btns_frame, text='9', fg='black', bg=num_color, width=5, height=2, command=lambda: button_click('9'))
multiply_btn = tk.Button(btns_frame, text='*', fg='black', bg=op_color, width=5, height=2, command=lambda: button_click('*'))

seven_btn.grid(row=2, column=0, padx=5, pady=5)
eight_btn.grid(row=2, column=1, padx=5, pady=5)
nine_btn.grid(row=2, column=2, padx=5, pady=5)
multiply_btn.grid(row=2, column=3, padx=5, pady=5)

# Third row
four_btn = tk.Button(btns_frame, text='4', fg='black', bg=num_color, width=5, height=2, command=lambda: button_click('4'))
five_btn = tk.Button(btns_frame, text='5', fg='black', bg=num_color, width=5, height=2, command=lambda: button_click('5'))
six_btn = tk.Button(btns_frame, text='6', fg='black', bg=num_color, width=5, height=2, command=lambda: button_click('6'))
minus_btn = tk.Button(btns_frame, text='-', fg='black', bg=op_color, width=5, height=2, command=lambda: button_click('-'))

four_btn.grid(row=3, column=0, padx=5, pady=5)
five_btn.grid(row=3, column=1, padx=5, pady=5)
six_btn.grid(row=3, column=2, padx=5, pady=5)
minus_btn.grid(row=3, column=3, padx=5, pady=5)

# Fourth row
one_btn = tk.Button(btns_frame, text='1', fg='black', bg=num_color, width=5, height=2, command=lambda: button_click('1'))
two_btn = tk.Button(btns_frame, text='2', fg='black', bg=num_color, width=5, height=2, command=lambda: button_click('2'))
three_btn = tk.Button(btns_frame, text='3', fg='black', bg=num_color, width=5, height=2, command=lambda: button_click('3'))
plus_btn = tk.Button(btns_frame, text='+', fg='black', bg=op_color, width=5, height=2, command=lambda: button_click('+'))

one_btn.grid(row=4, column=0, padx=5, pady=5)
two_btn.grid(row=4, column=1, padx=5, pady=5)
three_btn.grid(row=4, column=2, padx=5, pady=5)
plus_btn.grid(row=4, column=3, padx=5, pady=5)

# Fifth row
factorial_btn = tk.Button(btns_frame, text='!', fg='black', bg=sp_color, width=5, height=2, command=lambda: button_click('**2'))
zero_btn = tk.Button(btns_frame, text='0', fg='black', bg=num_color, width=5, height=2, command=lambda: button_click('0'))
dot_btn = tk.Button(btns_frame, text='.', fg='black', bg=num_color, width=5, height=2, command=lambda: button_click('.'))
equals_btn = tk.Button(btns_frame, text='=', fg='black', bg=op_color, width=5, height=2, command=calculate)

factorial_btn.grid(row=5, column=0, padx=5, pady=5)
zero_btn.grid(row=5, column=1, padx=5, pady=5)
dot_btn.grid(row=5, column=2, padx=5, pady=5)
equals_btn.grid(row=5, column=3, padx=5, pady=5)

# Run the main event loop
root.mainloop()
