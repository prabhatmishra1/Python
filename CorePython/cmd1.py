#Write a python script to handle command line arguments.
from sys import argv

s=0
argv.pop(0)
for i in argv:
     s=s+int(i)
print("sum of:",argv,"\n",s)
