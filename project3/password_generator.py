import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)
root.config(bg="black")
root.iconbitmap('project3/password_icon.png')
bg_image = tk.PhotoImage(file="project3/password_bg.png")

background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

length_var = tk.IntVar()
password_var = tk.StringVar()
include_lowercase_var = tk.BooleanVar()
include_uppercase_var = tk.BooleanVar()
include_digits_var = tk.BooleanVar()
include_symbols_var = tk.BooleanVar()
additional_characters_var = tk.StringVar()

include_lowercase_var.set(False)
include_uppercase_var.set(False)
include_digits_var.set(False)
include_symbols_var.set(False)

def generate_password(event=None):
    password_length = length_var.get()
    if password_length <= 0:
        messagebox.showerror("Error", "Password length must be greater than zero.")
        return
    
    character_set = ''
    if include_lowercase_var.get():
        character_set += string.ascii_lowercase
    if include_uppercase_var.get():
        character_set += string.ascii_uppercase
    if include_digits_var.get():
        character_set += string.digits
    if include_symbols_var.get():
        character_set += string.punctuation
    
    additional_characters = additional_characters_var.get()
    if additional_characters:
        character_set += additional_characters

    if not character_set:
        messagebox.showerror("Error", "Please select at least one character type.")
        return
    
    generated_password = ''.join(random.choice(character_set) for _ in range(password_length))
    password_var.set(generated_password)

def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard.")
    else:
        messagebox.showerror("Error", "No password generated to copy.")

# Password Length Dropdown
length_label = tk.Label(root, text="Password Length:",font=("Arial",10,"bold"),bg="#DA70D6")
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

length_options = [i for i in range(1, 21)]
length_combobox = ttk.Combobox(root, values=length_options, textvariable=length_var, state="readonly", width=5,font=("Arial",10,"bold"))
length_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="w")
length_combobox.current(0)

# Checkboxes for character types
checkbox_frame = tk.Frame(root,bg="#DA70D6")
checkbox_frame.grid(row=1, columnspan=4, padx=10, pady=5, sticky="w")
lowercase_checkbox = tk.Checkbutton(checkbox_frame, text="Lowercase", variable=include_lowercase_var,bg="#DA70D6",font=("Arial",10,"bold"))
lowercase_checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="w")
uppercase_checkbox = tk.Checkbutton(checkbox_frame, text="Uppercase", variable=include_uppercase_var,bg="#DA70D6",font=("Arial",10,"bold"))
uppercase_checkbox.grid(row=0, column=1, padx=5, pady=5, sticky="w")
digits_checkbox = tk.Checkbutton(checkbox_frame, text="Digits", variable=include_digits_var,bg="#DA70D6",font=("Arial",10,"bold"))
digits_checkbox.grid(row=0, column=2, padx=5, pady=5, sticky="w")
symbols_checkbox = tk.Checkbutton(checkbox_frame, text="Symbols", variable=include_symbols_var,bg="#DA70D6",font=("Arial",10,"bold"))
symbols_checkbox.grid(row=0, column=3, padx=5, pady=5, sticky="w")

 #Additional Characters Entry
additional_characters_label = tk.Label(root, text="Additional Characters:",font=("Arial",10,"bold"),bg="#DA70D6")
additional_characters_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

additional_characters_entry = ttk.Entry(root, textvariable=additional_characters_var, width=30)
additional_characters_entry.grid(row=2, column=1, padx=10, pady=5)

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password,font=("Arial"),bg="#DA70D6")
generate_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Generated Password Display
password_entry = ttk.Entry(root, textvariable=password_var, width=30,font=("Arial",15,"bold"),justify="center")
password_entry.grid(row=4, columnspan=4,rowspan=3, padx=10, pady=5)

# Copy to Clipboard Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard,font=("Arial"),bg="#DA70D6")
copy_button.grid(row=7, columnspan=2, padx=10, pady=5)

root.bind('<Return>', generate_password)

root.mainloop()
