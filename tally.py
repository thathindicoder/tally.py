from tkinter import *
from tkinter import ttk

# Make a window called root and set properties
root = Tk()
root.geometry('200x200')
root.title("Tally by Yousuf")

# Make a frame. I don't know how to describe this...
frm = ttk.Frame(root, padding=10)
frm.grid()

# This is the one (and most important) integer variable in the program.
num = 0

# TIME FOR GUI (pronounced 'Gooey')
ttk.Label(frm, text="Tally (by Yousuf)").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
numbereighter = ttk.Label(frm, text=num)
numbereighter.grid(column=0, row=3)

# This makes the +1 function
def plusone():
    global num
    num += 1
    numbereighter.config(text=num)
    
# RESET function
def reset():
    global num
    num = 0
    numbereighter.config(text=num)    

# Now to make the tally button itself...
tallybtn = ttk.Button(frm, text="+1", command=plusone)
tallybtn.grid(column=1, row=3)
resetbtn = ttk.Button(frm, text="Reset", command=reset)
resetbtn.grid(column=1, row=1)

root.mainloop()