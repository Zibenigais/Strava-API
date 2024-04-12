# Import module 
from tkinter import *

# Create object 
root = Tk() 

# Adjust size 
root.geometry( "375x100" ) 

w = Label(root, text ='Kādām sporta aktivitātēm vēlies piekļūt?', font = "50")  
w.pack()

def on_selection(value):
    global choice
    choice = value  # store the user's choice
    print(choice)
    root.destroy()  # close window
    
# Dropdown menu options 
options = [ 
    "Skriešanas", 
    "Riteņbraukšanas",
] 

# datatype of menu text 
clicked = StringVar() 

# initial menu text 
clicked.set( "Skriešanas" ) 

# Create Dropdown menu 
drop = OptionMenu( root , clicked , *options, command=on_selection ) 
drop.pack() 

# Execute tkinter 
root.mainloop()
