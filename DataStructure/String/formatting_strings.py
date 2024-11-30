"""
We will learn the formatting string:

We can format the strings with variable values by using replacement operator {} and format()
method.
The main objective of format() method to format string into meaningful output form
"""

# Case- 1: Basic Formatting for default, positional and keyword arguments
name='durga'
salary=10000
age=48
print("{} 's salary is {} and his age is {}".format(name,salary,age))
print("{0} 's salary is {1} and his age is {2}".format(name,salary,age))
print("{x} 's salary is {y} and his age is {z}".format(z=age,y=salary,x=name))


#Case-2: Formatting Numbers
"""
d--->Decimal IntEger
f----->Fixed point number(float).The default precision is 6
b-->Binary format
o--->Octal Format
x-->Hexa Decimal Format(Lower case)
X-->Hexa Decimal Format(Upper case)
"""

"""
Example-1: Decimal formatting
So :2d means 2 space will be added in string
:10d means 10 space
:012d means 12, 0 will add at front of 123
"""
print("Integer number is: {:2d}".format(123))  # '  123'
print("Integer number is: {:10d}".format(123)) # '        123 '
print("Integer number is: {:012d}".format(123)) # '000000000000123'


"""
Example-2: Float formatting where default precision is 6

precision means point ke bad ka number
"""
print("Floating number: {}".format(23.2321)) # normal printing hai

# As default precision is 6 so it will convert to 6
print("Floating number: {:f}".format(23.2321)) # 23.232100

# As default precision is 6 so it will convert to 6
print("Floating number: {:08.3f}".format(23.2321)) # 23.232100
