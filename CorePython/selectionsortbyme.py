def selectionSort(l):
   for i in range(len(l)):
       first=i;
       for j in range (i,len(l)):
            if l[j]<l[first]:
                first=j;
       (l[i],l[first])=(l[first],l[i])         
   return l    
print(selectionSort([4,5,2,1,3]))


