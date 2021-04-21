def factor(l):
    fact=[]
    for i in range(1,l+1):
        if l%i==0:
          fact=fact+[i]
    return fact


def sumPrime(arr):
    s=1
    for i in arr:
        if(factor(i)==[1,i]):
            s=s+i
    return s

print(sumPrime([1,2,3,4,5,9]))
    





