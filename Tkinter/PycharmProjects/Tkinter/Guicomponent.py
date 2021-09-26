from tkinter import *
obj=Tk()
obj.title("Gui components")
obj.geometry('500x500')
obj.wm_minsize(width=200,height=200)
obj.wm_maxsize(width=500,height=500)

b1=Button(obj,text="Button")
l1=Label(obj,text="Label")
e1=Entry(obj)
cb1=Checkbutton(obj,text="ok")
rb1=Radiobutton(obj,text="five")
t1=Text(obj)

#To visualize the component on the screen use pack method.
b1.pack()
l1.pack()
e1.pack()
cb1.pack()
rb1.pack()
t1.pack()





mainloop()