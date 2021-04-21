def prime(n):
    print("1 2 3",end=' ')
    for i in range(4,n+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i,end=' ')
        print(end='',sep=",")
    
n=int(input("Enter the value of n:"))
prime(n)
