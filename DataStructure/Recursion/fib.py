def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

'''
This function calculate sum of fib
'''

def fibsum(n):
    s=0
    for i in range(1,n+1):
            s=s+fib(i)
    return s

if __name__=="__main__":
    print(fibsum(5))            
