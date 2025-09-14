import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return

        characters = ""
        if var_letters.get():
            characters += string.ascii_letters
        if var_digits.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one option!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Error", "No password to copy!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.config(bg="#f2f2f2")

tk.Label(root, text="Password Length:", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
length_entry.pack(pady=5)

var_letters = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=var_letters, font=("Arial", 11), bg="#f2f2f2").pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=var_digits, font=("Arial", 11), bg="#f2f2f2").pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols, font=("Arial", 11), bg="#f2f2f2").pack(anchor="w", padx=20)


tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

password_entry = tk.Entry(root, font=("Arial", 12), width=25, justify="center")
password_entry.pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_password, font=("Arial", 12), bg="#2196F3", fg="white").pack(pady=5)

root.mainloop()