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

# we can the set the  proper position of any component
# we can the set the  width and height of any component also.
b1.place(x=10,y=20)
b2.place(x=70,y=20)
b3.place(x=150,y=20,width=40,height=40)


mainloop()