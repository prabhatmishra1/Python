def palindrom(x):
  m=len(x)
  for i in range(0,m//2):
    if(x[i]!=x[len(x)-1-i]):
        print("Not palindrom")
        break
  else:        
   if(i==(m//2)-1):
     print("its palindrom")
     
x=tuple(input("Enter value:"))
palindrom(x)

