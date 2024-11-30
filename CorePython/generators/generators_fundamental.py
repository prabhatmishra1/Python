"""
First lets understand the basic iterators and then will compare both
"""

def first_n(n):
    # It will take n numbers and return the list
    l = []
    while n > 0:
        l.append(n)
        n= n-1
    return l

# print(sum(first_n(n=1000000000000)))

"""
Conclusion: So we can see that we have to loop and load all
the value in the memory once that is not efficient

"""
# Now We will solve the same problem using generators

def first_n(n):
    # It will take n numbers and return the list
    while n > 0:
        yield n
        n= n-1

# it will return the generator function
generator = first_n(n=10)

# by using __next__ or next() can get one value at time

# first way to call
print(generator.__next__())
# second way to call
print(next(generator))
# convert into list
print(list(generator))
# do sum
print(sum(generator))

"""
we can turn a list comprehension into a generator expression by replacing
# the square brackets ("[ ]") with parentheses ( "( )")
"""

# list comprehension
l = [value for value in range(0, 10)]
print(l)

# generator comprehension
l = list((value for value in range(0, 10)))
print(l)
# every time you call it will return next value which does not load all the data in memory in one shot

# print(sum(first_n(n=10000)))

"""
Now lets understand what next does here?

Signature: next(iterator, default=some_value)
So next() is a function which take two argument this first is iterator and second is default
where if value not found in the iterator it will return the default value
"""

result = next(iter([value for value in range(10) if value==9 ]), "Not Found")
print(result)