from tkinter import *
obj=Tk()

obj.geometry("500x500")
obj.title('Frame')
obj.wm_minsize(width=200,height=200)
obj.wm_maxsize(width=400,height=400)
# creating frame

f1=Frame(obj,width=300,height=150,borderwidth=3,relief='solid')
f1.place(x=50,y=10)

f2=Frame(obj,width=300,height=150,borderwidth=3,relief='solid')
f2.place(x=50,y=200)

#set element on the frame
l1=Label(f1,text="id")
l1.place(x=10,y=10)
e1=Entry(f1)
e1.place(x=60,y=10)

l2=Label(f2,text="password")
l2.place(x=10,y=10)
e2=Entry(f2)
e2.place(x=70,y=10)
obj.mainloop()