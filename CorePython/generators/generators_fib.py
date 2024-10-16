''' Generate fibonacci series with python Generator'''

def fib(n):
    T1, T2 = 0, 1
    temp  = 0
    while n:
        yield T1
        T1 , T2 = T2, T1+T2
        n-=1

# convert into list
print(list(fib(10)))


