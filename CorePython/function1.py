# Take nothing,Return nothing.
'''def add():
    y,x=[eval(x)for x in input("Enter two values").split()]
    print("x=",x,"\ny=",y)
    print("Sum of %d and %d=%d"%(x,y,x+y))
add()'''

#Take something,Return nothing.
'''def add(a,b):
       print("x=",a,"\ny=",b)
       c=a+b
       print("Sum of",a,"and",y,"=",c)
y,x=[eval(x)for x in input("Enter two values:").split()]              
add(x,y)'''

# Take nothing,Return something.
'''def add():
    y,x=[eval(x)for x in input("Enter two values").split()]
    print("x=",x,"\ny=",y)
    z=x+y
    return z
q=add()
print("Sum={}".format(q))'''

#Take sometihng,Return something.
'''def add(a,b):
    c=a+b
    return c
y,x=[eval(x)for x in input("Enter two values").split()]
z=add(x,y)
print("x=",x,"\ny=",y)
print("Sum of {} and {}={}".format(x,y,z))'''

#When function returns nothing,it returns None value.
'''def add():
    c=10+20
z=add()
print("z=",z,type(z))#z=none'''

# keyword argument.
'''def f1(a,b):
    print("a=",a,"b=",b)

f1(10,20)#positional argument
f1(b=10,a=20)#keyword argument
f1(a=20,b=10)#same
f1(10,b=20)#a=10,b=20 no error
f1(a=10,20)#after keyword argument positional argument are not allowed.
f1(10,a=10)#f1 got miltiple value for a.
f1(a=10,a=20)#f1 got miltiple value for a.'''

#Variable length argument.
'''def avg(*n):
    print(n,type(n))
    s=0
    for i in n:
        s=s+i
    return s/len(n)    

x=avg(10,20,30)
print("avg=",x)'''

#variable length argument and normal argumet.

'''def f1(*points,playername):
      print(playername,end='')
      s=0
      for i in points:
          s=s+i
      print(" and points=",s)

f1(10,20,"prabhat")#f1() missing 1 required keyword-only argument: 'playername'
f1(playername="prabhat",10,20)#positional arguments follows keywordarguments.
f1(10,20,playername="prabhat")#no Error it corrcet.'''

#variable length argument and keyword argument.
'''def f1(**k):
    print("person information:")
    for key,value in k.items():
        print(key,"-",value)
f1(name="prabhat",age="21")
f1(name="Aman",marks="343")
f1(name="Ankur",salary="23234")'''    



  


 
