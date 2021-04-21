def prime(n):
    if(n==1):
        return 2 
    for i in range(n+1,n*2):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
           return i
           break
n=int(input("Enter the value of n:"))
m=prime(n)
print(m)
