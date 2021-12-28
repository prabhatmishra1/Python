def divide_by_zero(func):
    def inner(a,b):
        if b == 0:
            return "Opss cant divide"
        else:
           return  func(a,b)
    return inner

@divide_by_zero
def divide(a,b):
        c = a/b
        return c

if __name__ == "__main__":
    print(divide(2,1))