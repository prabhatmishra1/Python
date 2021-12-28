''' Generators is something like iterators and its more efficieant then iterator '''

def remote_channel():
    yield 'Start Gold'
    yield 'Set Max'
    yield 'Zee Cenema'

channel =  remote_channel()

# print(next(channel))
# print(next(channel))
# print(next(channel))
# print(next(channel))

# we can user for loop

# for value in remote_channel():
#     print(value)

# print 1 t0 10

def num_count(n):
    while n > 0:
        yield n
        n-=1

for i in num_count(10):
    print(i)


