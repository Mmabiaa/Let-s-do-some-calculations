# tkinter for Graphical user interface in python
from tkinter import * 
from tkinter import messagebox
import math

# Instance Of the class Tk() / Creating an object for the class Tk()
root = Tk()

# Window Customization
root.title("Simple Calculator By Group 10") # Title
root.geometry("600x700") # Size of the application
root.resizable(True, True) # Both Resizable True to allow user to resize the app 
root.configure(bg='pink')

# A Function To Create And Display Buttons
def create_buttons(root):
    # A list of Buttons
    buttons = [
        ('+', 1, 0), ('-', 1, 1), ('*', 1, 2), ('/', 1, 3), ('%', 1, 4), ('√', 1, 5),
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('cos', 2, 3), ('sin', 2, 4), ('tan', 2, 5),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('pi', 3, 3), ('x²', 3, 4), ('1/x', 3, 5),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('!', 4, 3), ('(', 4, 4), (')', 4, 5),
        ('0', 5, 0), ('.', 5, 1), ('log', 5, 2), ('DEL', 5, 3), ('=', 5, 4), ('C', 5, 5)
    ]
    
    # A for loop to help arrange the buttons in text, rows, and columns
    for (text, row, col) in buttons:
        if text == '=':
            bg_color = 'red'
            fg_color = 'white'
            bd = 20
        elif text == 'DEL':
            bg_color = 'orange'
            fg_color = 'white'
        elif text == 'C':
            bg_color = 'blue'
            fg_color = 'black'
        elif text in ['+', '-', '*', '/']:
            bg_color = 'orange'
            fg_color = 'black'
        elif text in ['1', '2', '3', '4','5', '6','7', '8', '9', '0', '.']:
            bg_color = 'grey'
            fg_color = 'white'
        elif text in ['cos', 'sin', 'tan', 'pi', 'x²', '1/x', '!', '(', ')', 'log']:
            bg_color = 'aqua'
            fg_color = 'black'
        else:
            bg_color = 'white'
            fg_color = 'black'
        

        # creating a button using the variable name 'button'
        button = Button(root, # Master or object of the class
                        text=text, # Assigning text to be equal to the text in the button list
                        font=("Arial", 18), # Setting font style and size
                        command=lambda t=text: on_button_click(t), # Assigning the command to pick each button click in the text and display it
                        fg=fg_color, # Setting foreground color 
                        bg=bg_color # Setting background color
                        )
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew") # Positioning the button using the grid() method

    # Allow the grid to be positioned relatively that when the window is resized, it picks the resized size
    for i in range(1, 6):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i-1, weight=1)

# A function to return True if user input is correct 
def on_button_click(char):
    if char == "=": # If user character clicked equals '=' 
        try: # If True / There is no error
            equation = str(eval(entry.get())) # To Evaluate User input into mathematics
            entry.delete(0, END) # Used to delete all user inputs
            entry.insert(END, equation) # Provides the answer which is assigned to the equation variable 
        except Exception as e: # If False / There is error 
            messagebox.showerror("Error", "Invalid Expression") # An error message should be displayed
            clear() # Calling the clear function to clear all user input
    elif char == "DEL":
        Backspace()
    elif char == "C":
        clear()
    elif char in ['sin', 'cos', 'tan', '√', 'x²', '1/x', 'log', 'pi', '!', '%']: # For advanced operations
        try:
            if char == 'sin':
                equation = str(math.sin(math.radians(float(entry.get()))))
            elif char == 'cos':
                equation = str(math.cos(math.radians(float(entry.get()))))
            elif char == 'tan':
                equation = str(math.tan(math.radians(float(entry.get()))))
            elif char == '√':
                equation = str(math.sqrt(float(entry.get())))
            elif char == 'x²':
                equation = str(math.pow(float(entry.get()), 2))
            elif char == '1/x':
                equation = str(1 / float(entry.get()))
            elif char == 'log':
                equation = str(math.log10(float(entry.get())))
            elif char == 'pi':
                equation = str(math.pi)
            elif char == '!':
                equation = str(math.factorial(int(entry.get())))
            elif char == '%':
                equation = str(float(entry.get())/100)
            entry.delete(0, END)
            entry.insert(END, equation)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            clear()
    else: # Else it should return to this
        entry.insert(END, char)

# A function To Clear All User Inputs
def clear():
    entry.delete(0, END) # Deletion of characters should start from the first and end at the last

# A function to delete only a specific part of the user input
def Backspace():
    entry.delete(len(entry.get())-1, END) # Access the length of the user input and starts deletion from the last character to left(-1)

# An Entry for user input
entry = Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

create_buttons(root)

root.mainloop()
