#Write a python script to find the greatest among three numbers.
print('"Enter three number to find greatest value:"\n')
x=int(input())
y=int(input())
z=int(input())
if x>y and x>z:
   print("%d is  greatest:\n"%x)
elif y>x and y>z:
    print("%d is greatest:\n"%y)
else:
   print("%d is  greatest:\n"%z)
