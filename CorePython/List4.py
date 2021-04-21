#write a python script to create the List of N prime Numbers.
n=int(input("Enter the value of nth prime number:"))
l=[1,2,3]
for i in range(4,n):
  for j in range(2,i):
      if(i%j==0):
          break
  else:
    l.append(i)
    
print("List of %dth prime number:"%n,l)    

      
        
