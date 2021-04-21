#Write a pyhton  script to manage the set.
s1=eval(input("Enter set A:"))
s2=eval(input("Enter set B:"))
l=eval(input("Enter List  :"))
s3=set(l)
s4=set()
y=0
print("A:",s1)
print("B:",s2)
print("Cardinality of n(A):",len(s1))
print("Cardinality of n(B):",len(s2))
print("A intersection B:",s1.intersection(s2))
print("A Union B:",s1.union(s2))
print("A Difference B:",s1.difference(s2))
print("A symmetric difference B:",s1.symmetric_difference(s2))
print("Cartision product of (A*B):")
for i in s1:
	for j in s2:
		#print("(",i,j,")",end=",",sep="")
		s4.add((i,j))
		
print(s4)		
print("\nFrequency of each element in List:")
for i in s3:
    y=l.count(i)
    print("{}={}".format(i,y))
