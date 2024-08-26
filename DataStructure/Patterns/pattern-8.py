#WAP to print this pattern
"""
========
1
2 3
3 4 5
4 5 6 7
========
"""

def print_pattern(n):
    for i in range(1, n+1):  #row
        row_value = i
        col = 1
        for j in range(col, i+1): #column
            print(row_value, end=" ")
            row_value+=1
            col+=1
        row_value+=1
        print(" ")

if __name__ == "__main__":
    n = 4
    print_pattern(n)

