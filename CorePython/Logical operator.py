Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 3>4 and 3==3
False
>>> 3<4 and 3==3
True
>>> 3<4 or 3>4
True
>>> 3>4 or 3!=0
True
>>> 3>2 or 3>1
True
>>> 3<2 or 3<1
False
>>> 5 and 4
4
>>> 5<1 and 4
False
>>> 0 and 4
0
>>> !5 and 4
SyntaxError: invalid syntax
>>> not 5 and 4
False
>>> 4 and 0
0
>>> 3 and 3.4
3.4
>>> 3 and "ab"
'ab'
>>> 3 and 5/0
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    3 and 5/0
ZeroDivisionError: division by zero
>>> 5/0 or 3
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    5/0 or 3
ZeroDivisionError: division by zero
>>> 5/0 or 3
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    5/0 or 3
ZeroDivisionError: division by zero
>>> 3 or 4
3
>>> 5 or 0
5
>>> 0 or 5
5
>>> not 4>3
False
>>> not 3
False
>>>  False True
SyntaxError: unexpected indent
>>> not "ab"
False
>>> not "ab"=="cd"
True
>>> not "ab"=="ab"
False
>>> not 3+4j
False
>>> 0+0j
0j
>>> not 0+0j
True
>>> 3 and x=4
SyntaxError: can't assign to operator
>>> 3 and x==4
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    3 and x==4
NameError: name 'x' is not defined
>>> 3 and x==4
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    3 and x==4
NameError: name 'x' is not defined
>>> x=4
>>> 3 and x==4
True
>>> 3 and 3+5
8
>>> 3 or 5/0
3
>>> 3 and 5/0
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    3 and 5/0
ZeroDivisionError: division by zero
>>> 5/0 and 3
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    5/0 and 3
ZeroDivisionError: division by zero
>>> ~6
-7
>>> ~8
-9
>>> ~56
-57
>>> ~-56
55
>>> ~1000
-1001
>>> 
