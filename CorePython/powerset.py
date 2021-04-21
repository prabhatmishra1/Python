s={1,2,3}
ps=[]

for i in range(8):
    for j in s:
        if(i & (1<<j)):
         print(j,end=' ')
    print(end=" ",sep=" ")
          
