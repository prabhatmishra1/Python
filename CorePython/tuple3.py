#Write a python script to check whether a tuple is subset of other tuple or Not.
t1=eval(input("Enter 1st set:"))
t2=eval(input("Enter 2nd set:"))
s1=set(t1)
s2=set(t2)
print("1st set is:",s1)
print("2nd set is:",s2)
print("{} is a subset of {}".format(s2,s1)) if s2.issubset(s1)else print(s2,"is not a subset of",s1) 
   

    
    

