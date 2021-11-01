def sayBye(func):
    def inner(name, data):
        print(name,data)
        if name == 'sunny':
            print(f'Bye {name}')
        else:
            func(name,data)  #call normal function
    return inner
@sayBye
def sayHi(name,data):
    print(f'Hi {name}')


if __name__ == '__main__':
   fun = sayBye(sayHi("sunny",10))
   print(fun.__name__)
