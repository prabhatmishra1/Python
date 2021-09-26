from tkinter import *
obj=Tk()

obj.title("Radiobutton")
obj.geometry("500x500")

#creating and placing the Radiobutton.

v=IntVar()#for grouping the radiobutton
rb1=Radiobutton(obj,text="Tea",variable=v,value=1)
rb2=Radiobutton(obj,text="Coffe",variable=v,value=2)
rb1.place(x=20,y=20)
rb2.place(x=60,y=20)
#creating and palcing the Radiobutton with preslecting butoon

v1=IntVar()#for grouping the radiobutton
rb3=Radiobutton(obj,text="Tea",variable=v1,value=1)
rb4=Radiobutton(obj,text="Coffe",variable=v1,value=2)
rb3.place(x=180,y=20)
rb4.place(x=220,y=20)
rb3.config(indicator=0,bg="cyan")#to change the look and feel.
rb4.config(indicator=0,bg='cyan')
obj.mainloop()
