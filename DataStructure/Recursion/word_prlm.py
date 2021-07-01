from collections import Counter
c=Counter('GOOGLE')

c=sorted(c.items())
for rnd in range(1, len(c)):
    for i in range(len(c)-rnd):
        if c[i][1] < c[i+1][1]:
            c[i],c[i+1]=c[i+1],c[i]
       
print(c)