def sayBye(func):
    # accept all the parameters which is passed to main function
    def inner(name, data):
        if name == 'sunny':
            return func(f'Bye {name}', data)
        else:
            return func(name, data)  #call normal function
    # print("inner", inner)
    return inner


# Add decorator
@sayBye
def sayHi(name, data):
    return f'Hi {name}'


if __name__ == '__main__':
    # First approach to call the function
    sayHi("sunny", 10)
    # fun = sayBye(sayHi("sunny",10))

