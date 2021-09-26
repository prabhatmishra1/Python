from tkinter import *
obj=Tk()
obj.title("Gui components")
obj.geometry('500x500')
obj.wm_minsize(width=200,height=200)
obj.wm_maxsize(width=500,height=500)

b1=Button(obj,text="Button")
b2=Button(obj,text="Button")
b3=Button(obj,text="Button")
b4=Button(obj,text="Button")

# grid() set the values in rows and column
# config used to set the  width and height of any component.
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=1,column=0)
b4.grid(row=1,column=1)
b1.config(width=20,height=5)
mainloop()