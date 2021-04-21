from tkinter import *
obj=Tk()
obj.title("Mouse Event")
obj.geometry('500x500')
obj.wm_minsize(width=200,height=200)
obj.wm_maxsize(width=500,height=500)

def f1(event):
   l1.config(text=("x="+str(event.x))+"y="+str(event.y))

l1=Label(obj,fg="blue",font=("calibri",14,"bold"))
l1.place(x=10,y=10)
obj.bind('<Motion>',f1)

obj.mainloop()
