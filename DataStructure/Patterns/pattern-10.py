#WAP to print this pattern
"""
========
A A A
B B B
C C C
C C C
========
"""

def print_pattern(n):
    for i in range(65, n+65):  #row
        print(f' {chr(i)} '*3)

if __name__ == "__main__":
    n = 4
    print_pattern(n)

