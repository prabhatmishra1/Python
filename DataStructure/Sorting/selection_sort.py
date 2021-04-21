def insertion_sort():
    l=[ int(input("Enter the elements %d :"%i)) for i in range(int(input("Enter the limit of n: ")))]
    for i in range(len(l)-2):
         min_index=find_min_value(l,i)
         l[i],l[min_index]=l[min_index],l[i]
    return l     

def find_min_value(l,start):
    m=l[start]
    index=start 
    for i in range (start,len(l)):
        if m>l[i]:
            m=l[i]
            index=i
    return index        
        


print(insertion_sort())    

