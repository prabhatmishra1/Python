Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # More on input:
>>> a,b,c=[eval(x) for x in input("Enter three value:").split(',')]
Enter three value:12,'abc',12.4
>>> a
12
>>> b
'abc'
>>> c
12.4
>>> type(a),type(b),type(c)
(<class 'int'>, <class 'str'>, <class 'float'>)
>>> a,b,c=[eval(x) for x in input("Enter three value:").split(' ')]
Enter three value:12,'abc',[12,3,4]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a,b,c=[eval(x) for x in input("Enter three value:").split(' ')]
ValueError: not enough values to unpack (expected 3, got 1)
>>> a,b,c=[eval(x) for x in input("Enter three value:").split(' ')]
Enter three value:12 'abc' [12,3,4]
>>> a
12
>>> b
'abc'
>>> c
[12, 3, 4]
>>> type(a),type(b),type(c)
(<class 'int'>, <class 'str'>, <class 'list'>)
>>> # How to enter List:
>>> l=[eval(x) for x in input("Enter value:").split(',')]
Enter value:12,'abc',12.4,3+4j
>>> l
[12, 'abc', 12.4, (3+4j)]
>>> # How to enter Tuple:
>>> t=tuple([eval(x) for x in input("Enter value:").split(',')])
Enter value:12,'abc',3+4j
>>> t
(12, 'abc', (3+4j))
>>> #How to enter set value:
>>> s=set([eval(x) for x in input("Enter value:").split(',')])
Enter value:12,'abc',3+4j
>>> s
{'abc', 12, (3+4j)}
>>> #How to enter dictionary:
>>> d=dict(input("Enter value:").split('-') for _ in range(3))
Enter value:1-prabhat
Enter value:2-Aman
Enter value:3-Ankur

>>> d
{'1': 'prabhat', '2': 'Aman', '3': 'Ankur'}
>>> d=dict(eval(input("Enter value:").split('-')) for _ in range(3))
Enter value:1-prabhat
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d=dict(eval(input("Enter value:").split('-')) for _ in range(3))
  File "<pyshell#24>", line 1, in <genexpr>
    d=dict(eval(input("Enter value:").split('-')) for _ in range(3))
TypeError: eval() arg 1 must be a string, bytes or code object
>>> d=dict(eval(input("Enter value:")).split('-') for _ in range(3))
Enter value:1-prabhat
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    d=dict(eval(input("Enter value:")).split('-') for _ in range(3))
  File "<pyshell#25>", line 1, in <genexpr>
    d=dict(eval(input("Enter value:")).split('-') for _ in range(3))
  File "<string>", line 1, in <module>
NameError: name 'prabhat' is not defined
>>> d=dict(x:input("Enter value:") for x in range(3))
SyntaxError: invalid syntax
>>> d={x:input("Enter value:") for x in range(1,3)}
Enter value:prabhat
Enter value:1212
>>> d
{1: 'prabhat', 2: '1212'}
>>> d=dict{input("Enter key:"):input("Enter value:") for x in range(3)}
SyntaxError: invalid syntax
>>> 
>>> d={input("Enter key:"):input("Enter value:") for x in range(3)}
Enter value:prabhat
Enter key:101
Enter value:Aman
Enter key:23
Enter value:avc
Enter key:233
>>> d
{'101': 'prabhat', '23': 'Aman', '233': 'avc'}
>>>  d={eval(input("Enter key:"):input("Enter value:")) for x in range(3)}
SyntaxError: unexpected indent
>>>  d={eval(input("Enter key:")):input("Enter value:") for x in range(3)}
SyntaxError: unexpected indent
>>>  d={eval(x)input("Enter key:"):input("Enter value:") for x in range(3)}
SyntaxError: unexpected indent
>>>  d={int(input("Enter key:")):input("Enter value:") for x in range(3)}
SyntaxError: unexpected indent
>>> d1={int(input("Enter key")):input("Enter value:")for x in range(3)}
Enter value:prabhat
Enter key12
Enter value:ass
Enter key23
Enter value:fgg
Enter key212
>>> d1
{12: 'prabhat', 23: 'ass', 212: 'fgg'}
>>> d1={eval(input("Enter key")):input("Enter value:")for x in range(3)}
Enter value:prabhat
Enter key'17mca'
Enter value:amna
Enter key1
Enter value:asa
Enter key23.5
>>> d1
{'17mca': 'prabhat', 1: 'amna', 23.5: 'asa'}
>>> 
