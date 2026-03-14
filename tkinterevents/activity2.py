from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry('400x400')
def msg():
    messagebox.showwarning('Warning', 'Stop virus has been found')
button=Button(root, text='Scan for virus', command=msg)
button.place(x=150, y=150)
root.mainloop()