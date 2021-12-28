''' make a decorator whic calculate the time taken by a function'''

import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(func.__name__+" function took "+ str(end_time-start_time)+" mili sec")
    return wrapper


@calculate_time
def count_value(n):
    for _ in range(n):
        print(_)

@calculate_time
def add_value():
    print(2+3)


if __name__ == '__main__':
    count_value(5)
    # add_value()