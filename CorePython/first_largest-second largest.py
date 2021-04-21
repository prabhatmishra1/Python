'''x=[int(input("Enter the %d elements: "%(i+1))) for i in range(int(input("Enter the size of list:")))]

fbig,sbig=(x[0],x[1],)
if sbig>fbig:
    sbig,fbig=fbig,sbig
print(fbig,sbig)

n=len(x)

for i in range(2,n):
    if x[i]>fbig:
        sbig=fbig
        fbig=x[i]
    elif x[i]>sbig:
        sbig=x[i]   
    

print(fbig,sbig)        
'''
x=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
m=x[0][1]
    for i in x:
        if i[1]<m:
            m=i[1]
            index=x.index(i)        
    x.pop(index)

    m=x[0][1]
    my=[]
    for i in x:
        if i[1]<=m:
            m=i[1]
            my.append(i[0])
    my.sort()
    for i in my:
        print(i)
