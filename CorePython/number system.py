Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=45
>>> print(x)
45
>>> x=101
>>> x
101
>>> x=0B101 # for binary number
>>> x
5
>>> x=0o10 #for octal  number
>>> x
8
>>> x=0x3f #for hexadecial number
>>> x
63
>>> print(hex(63))
0x3f
>>> print(bin(5))
0b101
>>> print(oct(10))
0o12
>>> x=0B101
>>> print(bin(x))
0b101
>>> y=bin(x)
>>> print(y[2::])
101
>>> print(y[3:::])
SyntaxError: invalid syntax
>>> print(y[3::])
01
>>> 
