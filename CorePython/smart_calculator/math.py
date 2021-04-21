from  math import  *
responses=["Welcome to smart calculator","My name is JARVIC","Thanks","sorry this is beyond my ability"]
def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
          l.append(float(t))
        except ValueError:
            pass


    return(l)

def add(a,b,):
    return(a+b)

def  sub(a,b,):
    return(a-b)

def mul(a,b):
   return(a*b)
def div(a,b):
    return(a/b)


def LCM(x,y):
    a=int(x)
    b=int(y)
    c= a if a>b else b 
    for i in range(c,a*b):
        if(i%a==0 and i%b==0):
            break;
    return i

def HCF(  x,y):
    a=int(x)
    b=int(y)
    z= a if a<b else b
    for i in range(z,0,-1):
        if(a%i==0 and b%i==0):
            break
    return i
def power(a,b):
    return a**b;
def s(a):
    return sin(a)
def c(a):
    return cos(a)
def t(a):
    return tan(a)
def l(a):
    return log(a)
def qrt(a):
    return sqrt(a)
def fact(a):
    return factorial(a)
def table(a):
    a=int(a)
    l=[]
    for i in range(1,11):
        l.append(a*i)
    return l
def sm():
    try:
       a=[eval(x) for x in input("Enter your List\n").split(' ')]
       print(fsum(a))
    except:
        print("Wrong Input:")
def st():
    s1=eval(input("Enter set A:"))
    s2=eval(input("Enter set B:"))
    s4=set()
    print("A:",s1)
    print("B:",s2)
    print("Cardinality of n(A):",len(s1))
    print("Cardinality of n(B):",len(s2))
    print("A intersection B:",s1.intersection(s2))
    print("A Union B:",s1.union(s2))
    print("A Difference B:",s1.difference(s2))
    print("A symmetric difference B:",s1.symmetric_difference(s2))
    print("Cartision product of (A*B):")
    for i in s1:
      for j in s2:
       s4.add((i,j))
    print(s4)		


def md(a,b):
    return fmod(a,b)
def ex():
  while True:  
   try: 
     x=input("Enter your mathmatical expression:\n")
     print("Write exit for exit.")
     print(eval(x))
   except:
       print("OO wrong input")
   if(x=='exit'):
        break     
        
    
def end():
    print(responses[2])
    input("Press enter key to exit:")
    exit()

def myname():
    print(responses[1])
def hello():
    print("Hello sir...");
def sorry():
    print(responses[3])
          
    
operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"+":add,"-":sub,"MINUS":sub,"SUBTRACTION":sub,"SUB":sub,
            "MULTIPLICATION":mul,"MULTIPLY":mul,"*":mul,"DIVISION":div,"DIVIDE":div,"/":div,
            "LCM":LCM,"HCF":HCF,"POWER":power,"MOD":md,"%":md}
calculations={"SIN":s,"COS":c,"TAN":t,"LOG":l,"FACT":fact,"FACTORIAL":fact,"SQRT":qrt,"TABLE":table,}
commands={"NAME":myname,"HELLO":hello,"END":end,"EXIT":end,"CLOSE":end,'LIST':sm,"SET":st,"SHELL":ex}
