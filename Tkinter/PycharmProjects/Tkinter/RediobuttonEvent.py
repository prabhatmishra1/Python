from tkinter import *
obj=Tk()

obj.geometry("500x500")
obj.title('RadiobuttonEvent')
obj.wm_minsize(width=200,height=200)
obj.wm_maxsize(width=400,height=400)

def setColor():

    l=['red','green','yellow']
    f1.config(bg=l[v1.get()-1])
#Creating Radiobutton
f1=Frame(obj,width=400,height=400,bg='black')
f1.place(x=0,y=0)
v1=IntVar()
r1=Radiobutton(f1,text='Red',fg='red',bg='black',variable=v1,value=1,command=setColor,borderwidth=0)
r2=Radiobutton(f1,text='Green',fg='green',bg='black',variable=v1,value=2,command=setColor,borderwidth=0)
r3=Radiobutton(f1,text='Yellow',fg='yellow',bg='black',variable=v1,value=3,command=setColor,borderwidth=0)

r1.place(x=30,y=10)
r2.place(x=100,y=10)
r3.place(x=180,y=10)


obj.mainloop()