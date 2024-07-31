from tkinter import * 
from tkinter import messagebox

#Instance Of the class Tk()
root = Tk()

#Window Customization
photo = PhotoImage(file='coupe.gif')
root.title("Let's Do Some Calculations")
root.geometry("400x500")
root.resizable(True, True) # Both Resizable False to prevent user from resizing the app size it's small  
root.iconphoto(True, photo) #Setting the app icon image to the variable 'photo' which contains the image file

#A function to return True if user input is correct 
def on_button_click(char):
    if char == "=": #If user character clicked equals '=' 
        try: #If True
            #It should solve for the answer
            equation = str(eval(entry.get()))
            entry.delete(0, END) #Used to delete all user inputs
            entry.insert(END, equation) #Used to insert characters after user input
        except Exception as e: #If False
            messagebox.showerror("Error", "Invalid Expression") #An error message show be displayed
            clear() #Calling the clear function to clear all user input
    else: #Else it should return to this
        entry.insert(END, char)

# A function To Clear All User Inputs
def clear():
    entry.delete(0, END) #Deletion of characters should start from the first and end at the last

#A function to delete only a specific part of the user input
def Backspace():
    entry.delete(len(entry.get())-1, END) #Access the length of the user input and starts deletion from the last character to left(-1)


# A Function To Create And Display Buttons 
def create_buttons(root):
    # A list of Buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
    ]
    #A for loop to help arrange the buttons in text, rows and columns
    for (text, row, col) in buttons:
        #creating a button using the variable name 'button'
        button = Button(root, #Master or object of the class
                        text=text, #Assigning text to be equal to the text in the button list
                        font=("Arial", 18), #Setting font style and size
                        command=lambda t=text: on_button_click(t), #Assigning the command to pick each button click in the text and display it
                        fg='orange', #Setting foreground of the button to orange 
                        bg='black' #Setting the Background of the button to black
                        )
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew") #Positioning the button using the grid() method
        '''
            row equals to the row position in the list
            column equals to the column position in the list
            padx, and pady to add padding 
            sticky = "nsew" means:
                    n = north, s = south, w = west, e = east  
                The sticky parameter specifies which sides of the cell the widget should stick to, 
                and it affects how the widget expands to fill the cell.
        '''

    backspace = Button( root, #As Master
                        text="DEL", #Assigning the text to be displayed in the button as DEL
                        font=('Times New Roman', 18), #Setting font Formatting
                        command= Backspace, #Assign the command to the Backspace Function
                        fg='black', #Setting foreground color as white
                        bg='orange', #Setting background color as orange
                        relief=RAISED, #Setting border behavior
                        bd=20 #Adding border with to be 20
                        )
    backspace.grid(row=5, column=3, rowspan=2) #Position: row 5, column 3 and and should over take 2 columns 

    clear_button = Button(root, #As Master
                          text="Clear All", #Assigning the text to be displayed in the button as C
                          font=("Arial", 18),  #Setting font Formatting
                          command=clear, #Assigning the command to the clear function
                          fg='red', #setting foreground color to red
                          bg='black', #setting background color to black
                          activebackground='black', #background after button is clicked,
                          activeforeground='white', #foreground after button is clicked
                          relief=RAISED, #Setting border behavior
                          bd=20 #Adding border with to be 20
                          )
    clear_button.grid(row=5, column=0, columnspan=3, sticky="nsew") #Position of the Grid  

    #ALlos the grid to be positioned relatively that when the window is resized, it picks the resized sized
    for i in range(1, 5):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i-1, weight=1)


   
#An Entry for user input
entry = Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

create_buttons(root)

root.mainloop()
