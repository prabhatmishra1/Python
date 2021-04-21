x=[10,12]
#print(x)
m=15
n=0
cnt=0
for i in range(1,3):
    n=m*i
    cnt=0
    for j in x:
      if(n%j==0):
          cnt+=1
    else:
        if(cnt==2):
            print(n)
    
    

