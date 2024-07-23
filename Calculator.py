import tkinter as tk
from tkinter import messagebox

def on_button_click(char):
    if char == "=":
        try:
            equation = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, equation)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            clear()
    else:
        entry.insert(tk.END, char)

def clear():
    entry.delete(0, tk.END)

def create_buttons(root):
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
    ]

    for (text, row, col) in buttons:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: on_button_click(t))
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    clear_button = tk.Button(root, text="C", font=("Arial", 18), command=clear)
    clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

    for i in range(1, 5):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i-1, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculator")
    root.geometry("400x500")
    root.resizable(False, False)
    
    entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge")
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    create_buttons(root)

    root.mainloop()