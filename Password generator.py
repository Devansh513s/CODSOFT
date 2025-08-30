import tkinter as tk
import random
import string
from tkinter import messagebox

# Function to generate a strong random password
def generate_password():
    try:
        length = int(entry_length.get())  # Get length from user input
        if length < 4:  # Minimum length check (4 characters)
            messagebox.showwarning("Input Error", "Password length should be at least 4 characters.")
            return
        
        # Create the set of characters (letters, digits, $, _, @)
        allowed_characters = string.ascii_letters + string.digits + "$_@"
        password = ''.join(random.choice(allowed_characters) for _ in range(length))
        
        # Display the generated password
        entry_password.config(state='normal')  # Allow changes to entry
        entry_password.delete(0, tk.END)  # Clear any existing text
        entry_password.insert(tk.END, password)  # Insert the new password
        entry_password.config(state='readonly')  # Make it readonly again to prevent user modification
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid number for password length.")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Title label
label_title = tk.Label(root, text="Strong Password Generator", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# Label for password length input
label_length = tk.Label(root, text="Enter Password Length:", font=("Arial", 12))
label_length.pack(pady=5)

# Input field for password length
entry_length = tk.Entry(root, font=("Arial", 14), width=10)
entry_length.pack(pady=10)

# Button to generate password
button_generate = tk.Button(root, text="Generate Password", font=("Arial", 14, "bold"), relief="flat", command=generate_password)
button_generate.pack(fill="x", pady=10, padx=20)

# Label for displaying the generated password
label_password = tk.Label(root, text="Generated Password:", font=("Arial", 12))
label_password.pack(pady=5)

# Entry field to display the generated password
entry_password = tk.Entry(root, font=("Arial", 14), width=30, state="readonly")
entry_password.pack(pady=10)

# Run the application
root.mainloop()
