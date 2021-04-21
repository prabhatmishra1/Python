def sortedarray(l,b=0):
    if len(l)==1:
        return
    temp=0
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
               temp=l[j]
               l[j]=l[j+1]
               l[j+1]=temp
                    
    sortedarray(l,len(l)-1)  






l=[eval(x) for x in input("Enter List of array,seprated by comma:").split(',')]
print(l)
sortedarray(l)

    
