Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3]
>>> li=iter(l)
>>> type(l)
<class 'list'>
>>> type(li)
<class 'list_iterator'>
>>> for i in iter(li):
	print(i)

	
1
2
3
>>> for i in (li):
	print(i)

	
>>> 
>>> while True:
	print(next(li))

	
Traceback (most recent call last):
  File "<pyshell#12>", line 2, in <module>
    print(next(li))
StopIteration
>>> li=iter(l)
>>> while True:
	print(next(li))

	
1
2
3
Traceback (most recent call last):
  File "<pyshell#16>", line 2, in <module>
    print(next(li))
StopIteration
>>> next(li)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    next(li)
StopIteration
>>> 
====================== RESTART: E:/python/generators.py ======================
>>> it=fib(5)
>>> next(it)
0
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    next(it)
  File "E:/python/generators.py", line 9, in fib
    a,b=a+b
TypeError: 'int' object is not iterable
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    next(it)
StopIteration
>>> it=fib(10)
>>> next(it),next(it),next(it),next(it),next(it)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    next(it),next(it),next(it),next(it),next(it)
  File "E:/python/generators.py", line 9, in fib
    a,b=a+b
TypeError: 'int' object is not iterable
>>> 
====================== RESTART: E:/python/generators.py ======================
>>> it=fib(5)
>>> next(it)
0
>>> next(it),next(it),next(it),next(it),next(it)
(1, 1, 2, 3, 5)
>>> next(it)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    next(it)
StopIteration
>>> it=fib(5)
>>> for i in it:
	print(i)

	
0
1
1
2
3
5
>>> 
>>> it=fib(5)
>>> while True:
	print(next(it))

	
0
1
1
2
3
5
Traceback (most recent call last):
  File "<pyshell#36>", line 2, in <module>
    print(next(it))
StopIteration
>>> 
