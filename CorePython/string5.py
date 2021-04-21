#Write a python script to cheack given string  is palindrom or Not.
s=input("Enter a string: ")
print("Given string is:",s)
print("Length  of Sring is: ",len(s))
m=len(s)
for i in range(0,m//2):
     if(s[i]!=s[m-1-i]):
       print('"Not a palindrom"')
       break  
else:
 print('"Its Palindrom"')
         
