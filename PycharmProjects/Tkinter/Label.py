from tkinter import *
obj=Tk()
obj.title("Gui components")
obj.geometry('500x500')
obj.wm_minsize(width=200,height=200)
obj.wm_maxsize(width=500,height=500)
#creating and placing the lablel.
l1=Label(obj,text="My name is ,prabhat")
l1.place(x=10,y=10)
#set size,foreground,background,broder,font,text.
l2=Label(obj,text="My name is Demo",width=20,height=1)
l2.config(bg="cyan",fg="yellow",font=("calibri",16,'bold'))
l2.place(x=200,y=20)
#set size using palce() border width and broder style.
l3=Label(obj,text="Third",bg="red")
l3.place(x=200,y=100,width="100",height="50")
#set Image,border-width,border-style

pic=PhotoImage(file='D:\cest.gif')
l4=Label(obj,text="prabhat",bg="cyan",image=pic,compound=CENTER,borderwidth=10,relief="solid")
l4.place(x=300,y=200)
mainloop()