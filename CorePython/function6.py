#write a python script to find sum of all even and odd numbers:
def cal(l):
    even=0
    odd=0
    for i in l:
        if(i%2==0):
            even=even+i
        else:
            odd=odd+i
    return even,odd
print("Enter the value of list:")
n=int(input())
l=[]
for i in range(n):
    l.append(int(input("Enter the value: ")))
even,odd=cal(l)
print("sum of even number=%d\nsum of odd number=%d"%(even,odd))
