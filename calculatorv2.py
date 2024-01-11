import tkinter as tk
from tkinter import ttk

def press(key):
    entry_text = entry.get()
    
    if key == 'C':
        entry.delete(0, tk.END)
    elif key == '=':
        try:
            result = eval(entry_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, key)

# Create a tkinter window
root = tk.Tk()
root.title("Calculator v2")
root.configure(bg='#864AF9')

# Entry widget to display the calculations and results
entry = tk.Entry(root, width=25, font=('Arial', 20), justify=tk.RIGHT, bd=5,)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create style for rounded buttons
style = ttk.Style()
style.configure('TButton', font=('Arial', 16), padding=5, borderwidth=0, foreground='black', background='#000000', relief=tk.FLAT)
style.map('TButton', foreground=[('pressed', 'black')], background=[('pressed', '#999999')])

# ぶとん
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '+', '='
]

row = 1
col = 0

for button in buttons:
    # if button != '=':
        ttk.Button(root, text=button, width=4, command=lambda key=button: press(key)).grid(row=row, column=col, padx=5, pady=5)
    # else:
    #     ttk.Button(root, text=button, width=10, command=lambda key=button: press(key)).grid(row=row, column=col, columnspan=2, padx=5, pady=5)
    
        col += 1
        if col > 3:
            col = 0
            row += 1

root.mainloop()
