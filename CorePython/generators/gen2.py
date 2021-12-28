''' Gerator fabonachi seris with python generator'''

def fib():
    T1, T2 = 0, 1
    temp  = 0
    while True:
        yield T1
        T1 , T2 = T2, T1+T2


for value in fib():
    if  value > 100:
        break
    print(value)







fib(5)