from tkinter import *
obj=Tk()

obj.geometry("500x500")
obj.title('Checkbutton')
obj.wm_minsize(width=200,height=200)
obj.wm_maxsize(width=400,height=400)

# creating and placing the Cheackbutton.

cb1=Checkbutton(obj)
cb1.place(x=10,y=10)

# creating border and caption of the Cheackbutton.

cb2=Checkbutton(obj,text="Agree")
cb2.config(borderwidth=2,relief='raised',fg="red",bg='cyan')
cb2.place(x=60,y=20)
obj.mainloop()
