m=[[1,2,3,4,5,6]]*6
l=[]
for k in range(16):
    s=0
    for i in range(3):
        for j in range(3):
            if i==1 and j==0 or i==1 and j==2:
                print(" ",end=" ")
                continue
            else: 
                print(m[i][j],end=" ")
                s=s+m[i][j]        
        print()
    l.append(s)    
    print("-------")
print(l) 
print(max(l))   