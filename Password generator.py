import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    try:
        length = int(entry_length.get())  
        if length < 4:  
            messagebox.showwarning("Input Error", "Password length should be at least 4 characters.")
            return
        
        allowed_characters = string.ascii_letters + string.digits + "$_@"
        password = ''.join(random.choice(allowed_characters) for _ in range(length))
        
        entry_password.config(state='normal') 
        entry_password.delete(0, tk.END) 
        entry_password.insert(tk.END, password) 
        entry_password.config(state='readonly') 
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number for password length.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

label_title = tk.Label(root, text="Strong Password Generator", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

label_length = tk.Label(root, text="Enter Password Length:", font=("Arial", 12))
label_length.pack(pady=5)

entry_length = tk.Entry(root, font=("Arial", 14), width=10)
entry_length.pack(pady=10)

button_generate = tk.Button(root, text="Generate Password", font=("Arial", 14, "bold"), relief="flat", command=generate_password)
button_generate.pack(fill="x", pady=10, padx=20)

label_password = tk.Label(root, text="Generated Password:", font=("Arial", 12))
label_password.pack(pady=5)

entry_password = tk.Entry(root, font=("Arial", 14), width=30, state="readonly")
entry_password.pack(pady=10)

root.mainloop()
