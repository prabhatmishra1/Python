x=5 # no need to define data type is dynamic typed
print(x)
x=2
print(x)

# cheacking  data type.
""" Data type is dependent on value of variable"""
x=print(type(x))
x=12.343
print(type(x))
x='c'
print(type(x))
x="prabhat"
print(type(x))

# cheacking  Id.
"""  variables conatins the adrress/reference of value.
      it does not create any memory block   """

x=23.4
print("Id of x:",id(x))
y=x;
print("Id of y:",id(y))
y=12;
print( "Id of y:",id(y))







