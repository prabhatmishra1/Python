from tkinter import *
screen=Tk()

def setAdditon():
    c=float(int(t1.get())+int(t2.get()))
    t3.delete('0', END)#to clear the text box
    t3.insert(0,str(c))

screen.title("Addition")
screen.wm_maxsize(width=400,height=400)
screen.wm_minsize(width=400,height=400)
screen.config(bg='gray',borderwidth='5',relief='groove')
#crating the Labels
l1=Label(screen,text='First number',font=('calibri',15,'bold'),bg='gray')
l2=Label(screen,text='Second number',font=('calibri',15,'bold'),bg='gray')
l3=Label(screen,text='Addition',font=('calibri',15,'bold'),bg='gray')
#creating the Entery
t1=Entry(screen,borderwidth=3,relief='groove')
t2=Entry(screen,borderwidth=3,relief='groove')
t3=Entry(screen,borderwidth=3,relief='groove')
#crating button
b1=Button(screen,text='Sum',borderwidth=3,relief='solid',width=20,command=setAdditon)

#palcing the component
l1.place(x=50,y=20)
l2.place(x=50,y=60)
l3.place(x=50,y=100)
t1.place(x=220,y=20)
t2.place(x=220,y=60)
t3.place(x=220,y=100)
b1.place(x=100,y=220)


screen.mainloop()