Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s="prabhat mishra"
>>> s
'prabhat mishra'
>>> s="Don't avoid practice"
>>> s
"Don't avoid practice"
>>> print(s)
Don't avoid practice
>>> s='  "prabhat mishra" '
>>> print(s)
  "prabhat mishra" 
>>> s=''' "Don't do that" '''
>>> s
' "Don\'t do that" '
>>> print(s)
 "Don't do that" 
>>> s=''' my
name
is
prabhat'''
>>> print(s)
 my
name
is
prabhat
>>> s='prabhat mishhra'#findind lenght.
>>> len(s)
15
>>> s.index(a) #finding index
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s.index(a) #finding index
NameError: name 'a' is not defined
>>> s.index('a')
2
>>> s.index("mishra")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.index("mishra")
ValueError: substring not found
>>> s.index('mishhra')
8
>>> s1.count('a') #finding occreance of particular charcter.
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s1.count('a') #finding occreance of particular charcter.
NameError: name 's1' is not defined
>>> 
>>> s.count('a')
3
>>> 
