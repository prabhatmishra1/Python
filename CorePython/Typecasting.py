Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x=5
>>> x
5
>>> str(x)
'5'
>>> x="prabhat"
>>> x
'prabhat'
>>> x="123"
>>> x
'123'
>>> y=int(x)
>>> y
123
>>> y=23
>>> z=x+y
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    z=x+y
TypeError: must be str, not int
>>> 
>>> x=2
>>> float(x)
2.0
>>> ord(x)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    ord(x)
TypeError: ord() expected string of length 1, but int found
>>> y=str(x)
>>> y
'2'
>>> ord(y)
50
>>> ord(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    ord(a)
NameError: name 'a' is not defined
>>> x='a'
>>> z
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    z
NameError: name 'z' is not defined
>>> x
'a'
>>> ord(x)
97
>>> a="123"
>>> b=50
>>> a
'123'
>>> b
50
>>> z=int(a)+ b
>>> z
173
>>> 
