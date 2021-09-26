from tkinter import *
obj=Tk()

obj.geometry("500x500")
obj.title('Canvas')
obj.wm_minsize(width=200,height=200)
obj.wm_maxsize(width=400,height=400)

#creating and placing the canvas
c=Canvas(obj,bg='gray',height=500)
c.place(x=10,y=20)
#creating the graphical object

c.create_line(0,10,400,10,fill='cyan',width=3)
c.create_rectangle(30,20,350,250,fill='lightgreen',outline='blue')
c.create_polygon(20,90,500,500,fill='red')
pts=[100,140,110,110,140,100,110,90,100,60,90,90,60,100,90,100]
c.create_polygon(pts,fill='red')

obj.mainloop()