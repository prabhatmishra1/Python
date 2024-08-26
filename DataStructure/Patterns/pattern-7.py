#WAP to print this pattern
"""
========
1
2 3 
4  5 6
7 8 9 10
========
"""

def print_pattern(n):
    cnt = 0
    for i in range(1, n+1):  #row
        for j in range(i): #column
            cnt+=1
            print(cnt, end=" ")
        print(" ")

if __name__ == "__main__":
    n = 4
    print_pattern(n)

