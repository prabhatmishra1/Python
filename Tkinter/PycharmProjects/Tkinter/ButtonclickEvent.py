from tkinter import *
obj=Tk()

obj.geometry("500x500")
obj.title('Frame')
obj.wm_minsize(width=200,height=200)
obj.wm_maxsize(width=400,height=400)

def msg1():
    l1.config(text='Good')

l1=Label(obj,text='Press the Button',font=('calibri',14,'bold'),fg='cyan')
l1.place(x=10,y=20)

b1=Button(obj,text='Press',borderwidth=2,relief='solid',width=10,command=msg1)
b1.place(x=50,y=80)

obj.mainloop()