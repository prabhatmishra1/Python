#WAP to print this pattern
"""
========
1
2 1
3 2 1
4 3 2 1
========
"""

def print_pattern(n):
    for i in range(1, n+1):  #row
        for j in range(i, 0, -1): #column
            print(j, end=" ")
        print(" ")

if __name__ == "__main__":
    n = 15
    print_pattern(n)

