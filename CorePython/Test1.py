def fib(n):
    if n!=0:
      print(fib(n-1)+fib(n-2))
    else:
        return 0
fib(5)
