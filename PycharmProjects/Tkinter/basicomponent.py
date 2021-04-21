from tkinter import *
obj=Tk()
obj.title("Gui components")
obj.geometry('500x500')
obj.wm_minsize(width=200,height=200)
obj.wm_maxsize(width=500,height=500)


# set the size at the time of creation only.
b1=Button(obj,text="Button",width=20,height=3)#it support in char
b1.place(x=10,y=30,width=50,height=50)# it supports in pixels.
b1.config(bg="black",fg="white")
mainloop()