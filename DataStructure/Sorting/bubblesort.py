'''def bubble_sort():
    l=[int(input("Enter the %d number: "%i)) for i in range(int(input("Enter the n limit: ")))]

    for i in range(len(l)):
      for j in range(len(l)-1-i):# har bar round kam ho rha hai len(l)-1-i
        if l[j]>l[j+1]:
         l[j],l[j+1]=l[j+1],l[j] #swaping in python
    print(l,i)            
bubble_sort()'''


def modified_bubble_sort():
    l=[int(input("Enter the values of %d: "%i))  for i in range(int(input("Enter the n limit :")))]
    flag=True
    for i in range(len(l)):
        if (flag==False):
            return 
        for j in range(len(l)-1):
            if l[j]>l[j+1]:
               flag=True 
               l[i],l[j+1]=l[j+1],l[i]        
    return l     

print(modified_bubble_sort())

    

