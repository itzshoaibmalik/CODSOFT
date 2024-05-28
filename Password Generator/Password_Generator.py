# Shoaib Malik
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def reset_fields():
    user_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Main windoww
root = tk.Tk()
root.title("Password Generator")
root.geometry("420x280")
root.resizable(False, False)

title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), fg="dark green")
title_label.pack(pady=10)

frame = tk.Frame(root, padx=20, pady=10)
frame.pack(pady=10)


tk.Label(frame, text="Enter user name:").grid(row=0, column=0, sticky=tk.W, pady=5)
user_entry = tk.Entry(frame, width=35)
user_entry.grid(row=0, column=1, pady=5)


tk.Label(frame, text="Enter password length:").grid(row=1, column=0, sticky=tk.W, pady=5)
length_entry = tk.Entry(frame, width=35)
length_entry.grid(row=1, column=1, pady=5)


tk.Label(frame, text="Generated password:").grid(row=2, column=0, sticky=tk.W, pady=5)
password_entry = tk.Entry(frame, width=35)
password_entry.grid(row=2, column=1, pady=5)


generate_btn = tk.Button(root, text="Generate Password", bg="dark green", fg="white", command=generate_password)
generate_btn.pack(pady=10)


bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)


accept_btn = tk.Button(bottom_frame, text="Accept", bg="green", fg="black", command=root.quit)
accept_btn.grid(row=0, column=0, padx=20)


reset_btn = tk.Button(bottom_frame, text="Reset", bg="red", fg="black", command=reset_fields)
reset_btn.grid(row=0, column=1, padx=20)


root.mainloop()
