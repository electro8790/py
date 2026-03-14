from tkinter import *
import random
root=Tk()
root.geometry('400x400')
colors=['red', 'green', 'blue', 'yellow', 'orange', 'purple']
def changecolor():
    color=random.choice(colors)
    root.config(bg=color)
button1=Button(root,text='Change color',command=changecolor)
button1.place(x=80,y=80)
count=0
def counterincrease():
    global count
    count=count+1
    lbl1=Label(root,text=str(count))
    lbl1.place(x=190,y=120)
button2=Button(root,text='increase count',command=counterincrease)
button2.place(x=80,y=120)
root.mainloop()   