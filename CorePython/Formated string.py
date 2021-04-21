# print variable.
x=10
print(x)

# print Multipal value using sep.
y=20
print(x,y)
print(x,",",y)#stil space.
print(x,y,sep="");# Without space.
print(x,y,sep=":");
print(x,y,sep=",");
print("prabht"+"mishra");
print("prabht","mishra");
print("prabht","mishra",sep="\n");

# print() is like println().
print(x)
print(y)
# use of End.
print(x,end="")
print(y)
print(x,end=":::")
print(y)
# sep and end togather.
z=30
print(x,y,z,end=".",sep=":");
# Formated string.
print("The value of %d is"%x)
print("sum of %d and %d= %d"%(x,y,z));
# Replacement operator.

s="prabhat"
print("hello,",s,"x=",x,"y=",y);#space will come.
print("hello,{}x={}y={}".format(z,x,y));
print("hello,{}x={}y={}".format(x,z,y));
#print("hello,{z}x={x}y={y}".format(z,x,y));#  Error.
print("hello,{z}x={x}y={y}".format(z="Golu",x=1,y=2));




