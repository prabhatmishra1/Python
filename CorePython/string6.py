#Write a python script to find a pattern in given string:
s=input("Enter the strings: ")
ptr=input("Enter the pattern of String: ")
cnt=0
if ptr in s:
    cnt=s.count(ptr)
    start=s.index(ptr)
    aux=ptr[-1]
    end=s.index(aux)
    print("Pattern is in string:")
    print("Total occureence of given  pattern  is:",cnt)
    print("starting index and ending index of the pattern is[%d,%d]:"%(start,end))
else:
    print("Pattern is not in string:")
