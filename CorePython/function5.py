def string(x):
    cnt=0
    s=set(x)
    d={}
    for i in s:
       cnt=x.count(i)
       #print(i,"=",cnt)
       d[i]=(cnt) 
    return d 





x=input("Enter a string: ")
l=string(x)
print(l)
    

