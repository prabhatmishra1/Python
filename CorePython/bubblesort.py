def bubbleSort(l):
    for i in range(1,len(l)):
     for j in range (0,len(l)-i):
          if l[j]>l[j+1]:
              (l[j],l[j+1])=(l[j+1],l[j])
    return l        
             
print(bubbleSort([5,3,4,5,5,6,4,4]))
