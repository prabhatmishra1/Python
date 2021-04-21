def string(x):
    cnt=0
    s=set(x)
    d={}
    for i in s:
       cnt=x.count(i)
       #print(i,"=",cnt)
       d[i]=(cnt) 
    return d 





x=eval(input("Enter Tuple:"))
l=string(x)
print("Frequency in the tuple:")
print(l)
    

