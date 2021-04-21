Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for e in range(5)
SyntaxError: invalid syntax
>>> for e in range(5):
	print(e)

	
0
1
2
3
4
>>> print(range(5))
range(0, 5)
>>> for x in range(10)
SyntaxError: invalid syntax
>>> 
>>> for x in range(10):
	print(x)

	
0
1
2
3
4
5
6
7
8
9
>>> y=range(10)
>>> for e in range y:
	
SyntaxError: invalid syntax
>>> for e in y:
	print(e)

	
0
1
2
3
4
5
6
7
8
9
>>> for e in range(3.3)
SyntaxError: invalid syntax
>>> for e in range(3.3):
	print(e)

	
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    for e in range(3.3):
TypeError: 'float' object cannot be interpreted as an integer
>>> for e in range(5,10):
	print(e)

	
5
6
7
8
9
>>> for e in range(10,5):
	print(e)

	
>>> # blank output
>>> range(1,20,2)
range(1, 20, 2)
>>> for i in range(1,20,2):
	print(i)

	
1
3
5
7
9
11
13
15
17
19
>>> for i in range(2,20,4)
SyntaxError: invalid syntax
>>> for i in rnage(2,20,4):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    for i in rnage(2,20,4):
NameError: name 'rnage' is not defined
>>> for i in rnage(2,20,4):
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    for i in rnage(2,20,4):
NameError: name 'rnage' is not defined
>>> for i in range(2,4,20):
	print(i)

	
2
>>> for i in range(1,-10)
SyntaxError: invalid syntax
>>> for i in range(1,-10):
	print(i)

	
>>> for i in range(1,-10,-1):
	print(i)

	
1
0
-1
-2
-3
-4
-5
-6
-7
-8
-9
>>> for i in range(20,0,-1):
	print(i)

	
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
>>> 
