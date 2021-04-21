#Write a python script to understand about iterators.

def fib(n):
    a,b,c=0,1,0
    while True:
        if c>n:
            return
        yield a
        a,b=b,a+b
        c+=1
