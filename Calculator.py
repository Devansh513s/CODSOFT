import tkinter as tk

def click(button_text):
    """Handles button click events"""
    current = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("330x460")
root.resizable(False, False)

# Entry widget (Display)
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.pack(fill="both", padx=10, pady=10, ipadx=8, ipady=12)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        button = tk.Button(frame, text=btn, font=("Arial", 18), command=lambda b=btn: click(b))
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)

root.mainloop()

