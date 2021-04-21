# Write a python script to count the  vowels in string.
s=input("Enter a string:-")
print("Given string is:",s)
l=[]
cnt=0
y=0
s1=0
for i in s:
    y=s.count(i)
    if i  in l:
     pass
    else:
     l.append(i)
     print(i,"=",y)
     
    
print("String without duplicate characters:-",end='')
for i in l:
     print(i,end="")
     if('a' in i or 'i' in i or 'o' in i or'u' in i or'A' in i or'E' in i or'I' in i or'O' in i or'U'in i):
           cnt+=1
print("\nTotal numbers  of vowels is:",cnt)
