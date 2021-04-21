#Write a python script to print distinct elements along with their frequncy of occurrence in the list.

x=eval(input("Enter List:"))
l=[]
for i in x:
     y=x.count(i)
     if  i in l:
         pass
     else:
         l.append(i)
         print(i,"=",y)
print(l)
