# # syntax of lambda =>  lambda arguments: calulation
# # syntax of filter=> filter(function, iterables)
# from functools import reduce
# l = ['prabhat', 'ram', 'sonu', 'rajan']

# print(reduce(lambda x,y:x+y,l))

# if __name__ == "__main__":
#     pass


def isPrime(n):
    if n <= 1:
        return "Invalid Number"
    else:
        for i in range(n-1,1,-1):
            if n%i==0:
             return False
        else:
            return True

if __name__ == "__main__":
   l = [2,3,4,5,6,7,8,9,10,11]
   print(list(filter(isPrime , l)))