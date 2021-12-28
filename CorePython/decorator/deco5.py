# def deco(func):
#     def wrapper(x,y):
#         return func((x**2),(y**2))
#     return wrapper


# @deco
# def fun(x,y):
#     return x+y

# if __name__== '__main__':
#     print(fun(2,5))


# from typing import AsyncGenerator


# def fib(curr,prev=None):
#     if not curr:
#         return 0
#     return curr+prev



# #Join in sql->
# # user table

# first_name last_name age
# Ram          mishra  21
# Ram          yadav    90

#aggrigate
#annotate
#custom middleware
#TestCase
#logger in djano check for architecture and lib(kuberntes)
# Alhorithm

def mat(arr):
    n = len(arr)
    left = 0
    right = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                left+=arr[i][j]
                # print(arr[i][j])
            if (n-1)-i == j:
                right+=arr[i][j]
                # print(arr[i][j])
    print(left)
    print(right)
    return abs(left-right)

if __name__== '__main__':
   arr = [[1,2], [3,10]]
   n = 2
   print(mat(arr))


