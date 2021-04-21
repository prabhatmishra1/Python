# writing in file
string=input("Enter the string: ");
f=open("E:\\python\\FileHandling\\prabhat.txt",'w');
f.write(string);#simple string
l=["prabhat|","mishra|","Amana"]
f.writelines(l);#it takes list object only.

f.close();
