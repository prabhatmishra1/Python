from tkinter import*

screen=Tk()

screen.title("Text-box")
screen.geometry('500x500')
screen.wm_minsize(width=200,height=200)
screen.wm_maxsize(width=500,height=500)

#creating and placing a text box

e1=Entry(screen)
e1.place(x=20,y=20)

#creating,placing,sizing ,font ,color,border

e2=Entry(screen)
e2.place(x=20,y=60)
e2.config(borderwidth=2, relief='solid',font=("calibri",10),fg="blue", bg="cyan")

#creating Entery default text and non editable

e3=Entry(screen)
e3.insert(0,'enter here')
e3.place(x=20,y=100)
e3.config(state=DISABLED)


screen.mainloop()
