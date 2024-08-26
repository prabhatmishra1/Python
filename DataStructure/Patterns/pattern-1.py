#WAP to print this pattern
"""
========
* * * *
* * * *
* * * *
* * * *
========
"""

def print_pattern():

    for i in range(4):  #row
        for j in range(4): #column
            print(" * ", end="")
        print(" ")


if __name__ == "__main__":
 
    print_pattern()

