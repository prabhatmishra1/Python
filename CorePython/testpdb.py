import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'it tooks {(end-start)} times')
        return result
    return wrapper

@time_it
def fun1():
    start = time.time()
    sum = 0
    for i in range(1,10):
        sum = sum+i
    end = time.time()
    print(sum)
#     print(f'it tooks {(end-start)*1000} times')


@time_it
def fun2():
    sum = 0
    for j in range(1,10):
        for i in range(1,10):
            sum = sum+i
    print(sum)

def add(a, b):
    s = a+b
    return s


def fib(n):
   p, q = 0, 1
   while(p < n):
       yield p
       p, q = q, p + q

if __name__ == '__main__':
    x = fib(10)
    print(x)
