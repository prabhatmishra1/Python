#WAP to print this pattern
"""
========
1
2 2
3 3 3
4 4 4 4
========
"""

def print_pattern(n):
    for i in range(1, n+1):  #row
        print(f"{str(i)*i}")
        

if __name__ == "__main__":
    n = 5
    print_pattern(n)

