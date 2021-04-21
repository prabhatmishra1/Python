# sumn of natural sqare number by recurtion.
def sum(n):
	if n==1:
		return 1
	return n**2+sum(n-1)
n=int(input("Enter the value of n:"))
s=sum(n)
print("Sum of first square %d is %d"%(n,s))
