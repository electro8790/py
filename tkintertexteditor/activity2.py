from tkinter import *
window=Tk()
window.title('Letter counter')
window.geometry('400x600')
lbl1=Label(window,text="Enter a word")
lbl1.pack()
entry1=Entry(window,width=20)
entry1.pack()
def count():
    text=str(entry1.get())
    textlength=len(text)
    lbl2=Label(window,text=f"Number of letters: {textlength}")
    lbl2.place(x=100,y=200)
    return textlength
button1=Button(window,text="count the letters",command=count)
button1.pack()



window.mainloop()

