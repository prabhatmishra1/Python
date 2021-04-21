f=open("E:\\python\\FileHandling\\prabhat.txt","r+")

a='aman\n'
l=[]
while True:
    s=f.readline()
    if s=='':
        break
    if s!=a:
      l.append(s)
    if s==a:
        print("string found:");
        l.append("AMAN\n")
    
    print(s);
f.close();
f=open("E:\\python\\FileHandling\\prabhat.txt","w")

f.writelines(l);
f.close();
print(l)
