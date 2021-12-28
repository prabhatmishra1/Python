
def deco(func):
    def wrapper(*args, **kwargs):
        print("deco starts")
        return func(*args , **kwargs)
        # print("doco end")
    return wrapper
@deco #means fun = deco(func)
def func(name):
   print("func start")
   return "Hello"

if __name__ ==  "__main__":
    # fun  = deco(func)
    res   = func('asas')
    print(res)