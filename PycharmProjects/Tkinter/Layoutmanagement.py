from tkinter import *
obj=Tk()
obj.title("Gui components")
obj.geometry('500x500')
obj.wm_minsize(width=200,height=200)
obj.wm_maxsize(width=500,height=500)

b1=Button(obj,text="Button",bg="cyan")#bg used for color.
b2=Button(obj,text="Button",bg="cyan")
b3=Button(obj,text="Button")
b4=Button(obj,text="Button")
b5=Button(obj,text="test")

#To visualize the component on the screen use pack method.
b1.pack(side=RIGHT) # side can placed according to screen.
b2.pack(side=TOP,fill='x')#fill occupy the screen size x=(horizentaly)
b3.pack(side=LEFT,fill='y')#fill occupy the screen size y=(verticly)
b5.place(x=300,y=100)
#padding .

b4.pack(side=BOTTOM,padx=10,pady=20)#padx means external padding.

b4.pack(side=BOTTOM,ipadx=10,ipady=20)#ipadx means internal padding.




mainloop()