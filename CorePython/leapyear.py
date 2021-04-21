#Write a python script to cheack if a year is leap year or not.
print('"Enter the year  ton cheack if a year is leap year or not."\n')
x=int(input())
if (x%400==0 or x%100!=0) and (x%4==0):
   print("%d is  Leap year:\n"%x)
else:
   print("%d is not  Leap year:\n"%x)
