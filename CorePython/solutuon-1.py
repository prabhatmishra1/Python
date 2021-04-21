#Write a program  to generate magic square matrix (4*4),filled with 16 consecutive number,where the first number from 16 consecutive number is entered by user.
try:
    x=int(input("Enter a number:"))
    l=[[x+0,x+14,x+13,x+3],
        [x+11,x+5,x+6,x+8],
        [x+7,x+9,x+12,x+4],
        [x+18,x+2,x+1,x+15]]
    print(l)
    for i in l:
        for j in i:
            print("%3d"%j,end="")
        print()      
except:
    print("Invalid number:")
