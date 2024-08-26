#WAP to print this pattern
"""
========
*
* *
* * *
* * * *
========
"""

def print_pattern(n):
    
    for i in range(1, n+1):  #row
        print(" * "*i)

if __name__ == "__main__":
    n = 4
    print_pattern(n)

