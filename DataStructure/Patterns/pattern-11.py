#WAP to print this pattern
"""
========
A B C
A B C
A B C
========
"""

def print_pattern(n):
    for i in range(n):  #row
        print(f'{chr(65)} {chr(65+1)} {chr(65+2)}')

if __name__ == "__main__":
    n = 3
    print_pattern(n)

if __name__ == "__main__":
    n = 4
    print_pattern(n)

