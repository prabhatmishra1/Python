x=int(input("Enter smaller number"))
y=int(input("Enter larger number"))

for i in range(x,y):
  for j in range(2,i):
      if(i%j==0):
       break
    
  else:
   print(x,"is prime number")
   break


      
