#Write a python script to take month value in  numeric formate and display number of days in it.
print('"Enter month value in  numeric formate  to cheack number of days in it"\n')
x=int(input())
if x>12 or x<=0:
   print("%d is  Not correct month:\n"%x)
elif x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
   print("%d month has 31  days:\n"%x)
elif x==2:
    print("%d month has 28 or 29 days:\n"%x)
else:
    print("%d month has 30  days:\n"%x)
