import tkinter
import datetime
window=tkinter.Tk()
window.title('starting with widgets')
window.geometry('500x600')
lbl=tkinter.Label(window,text='Hey there',fg='white',bg="#072f5f",height=1,width=300)
name_lbl=tkinter.Label(text='full name',bg="#3895D3")
name_entry=tkinter.Entry()
def display():
    name=name_entry.get()
    global message
    message="welcome to the application! \nToday's date is:"
    greet="hello "+name+"\n"
    text_box.insert(tkinter.END,greet)
    text_box.insert(tkinter.END,message)
    text_box.insert(tkinter.END,datetime.datetime.now())
text_box=tkinter.Text(height=3)
btn=tkinter.Button(text='begin',command=display,fg='white',bg="#3895D3")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

window.mainloop()