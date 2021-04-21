Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 3>4
False
>>> 4<3
False
>>> 4>3
True
>>> x=True
>>> y=int(x)
>>> y
1
>>> int(False)
0
>>> bool(4)
True
>>> bool(5)
True
>>> bool(0)
False
>>> bool(True)
True
>>> y=int(bool(4))
>>> y
1
>>> bool(False)
False
>>> bool(None)
False
>>> "ab">"cd"
False
>>> "ab<cd"
'ab<cd'
>>> 
>>> "ab"<"cd"
True
>>> 'prabhat'<'mishra'
False
>>> "prabhat"=="prabhat"
True
>>> "prabhat"=="mishra"
False
>>> 3+4j>2+3j
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    3+4j>2+3j
TypeError: '>' not supported between instances of 'complex' and 'complex'
>>> 3+4j==3+2j
False
>>> 3+4j==3+4j
True
>>> x=5
>>> x
5
>>> x=True+x
>>> x
6
>>> x=True+True+x;
>>> x
8
>>> 5>4>3bool(True)
SyntaxError: invalid syntax
>>> 5>3>2>1
True
>>> 5>4>3>2<1
False
>>> "a">=97
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    "a">=97
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> "a"==97
False
>>> ord("a")==97
True
>>> 3+4j==3+4j
True
>>> 5==5.0
True
>>> 5==5.1
False
>>> True==1
True
>>> True==5
False
>>> True>5
False
>>> True=5
SyntaxError: can't assign to keyword
>>> 5.0<6.0
True
>>> True!=False
True
>>> 
