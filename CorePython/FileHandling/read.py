#reading in file
f=open("E:\\python\\FileHandling\\prabhat.txt",'r')
#print(f.read())# it reads all char in one shot.

#print(f.read(5))# 5 char in one shot til eof.

#readline method.

# it read line by line

'''s1=f.readline();
print(s1)

s2=f.readline();
print(s2)'''

# read by loop
'''while True:
        s1=f.readline()
        if s1=='':
            break
        print(s1);
print("EOf");
f.close();   '''

# readlines method

l=f.readlines();#it returns lines as list.
print(l);
