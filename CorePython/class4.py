''' Define a class to store book related information like bookid,title,price,author,publisher.define function to input,show,change
    price'''
class book:
    def input(self,a,b,c):
        self.bookid=a
        self.title=b
        self.price=c
    def show(self):    
        print(self.bookid,self.title,self.price,sep="\n")
    def changeprice(self):
        a=eval(input("Enter new price value for the book:"))
        self.price=a
        self.show()
a,b,c=eval(input("Enter bookid,title and price:"))        
obj1=book()
obj1.input(a,b,c)
obj1.show()
obj1.changeprice()


