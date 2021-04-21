def lcm(*t):
    if 0 in t:
        return 0
    if min(t)<0:
        return -1
    L,p,l=1,2,list(t)
    while max(l)!=1:
        flag,i=0,0
        while i<len(l):
            if l[i]%p==0:
              l[i]/=p
              flag=1
            i+=1
        if flag==0:
            p=nextprime(p)
        else: 
            L*=p
    return L
def nextprime(n):
    x=n+1
    while True:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                break
        else:
            return x
        x+=1 
            
         
