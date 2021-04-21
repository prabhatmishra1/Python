'''def outer():
    print("outer function is comming")
    a=10
    def inner():
       print("inner function started %d" %a)
       b=30
       
    return inner


f1=outer()

f1()'''

'''def decor(func):
    def inner(n):
        if n==0:
            print("not")
        else:
            func(n)
    return inner
             
@decor
def   dis():
    print(n)

dis(0)'''


def smart_div(func):
    def  wrapper(a,b):
        if b==0:
         print("cant")
        else:
           func(a,b)
    return wrapper      

def div(a,b):
    print(a/b)


m1=smart_div(div)
m1(20,30)    


    
