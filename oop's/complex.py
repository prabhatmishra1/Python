"""
Problem statement
A ComplexNumber class contains two data members: one is the real part (R) and the other is imaginary (I) (both integers).

Implement the Complex numbers class that contains the following functions -

1. constructor
You need to create the appropriate constructor.

2. plus -
This function adds two given complex numbers and updates the first complex number.

e.g.

if C1 = 4 + i5 and C2 = 3 +i1
C1.plus(C2) results in:
C1 = 7 + i6 and C2 = 3 + i1
3. multiply -
This function multiplies two given complex numbers and updates the first complex number.

e.g.

if C1 = 4 + i5 and C2 = 1 + i2
C1.multiply(C2) results in:
C1 = -6 + i13 and C2 = 1 + i2
4. print -
This function prints the given complex number in the following format :

a + ib
Note: There is space before and after '+' (plus sign) and no space between 'i' (iota symbol) and b.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
4 5
6 7
1
Sample Output 1 :
10 + i12
Sample Input 2 :
4 5
6 7
2
Sample Output 2 :
-11 + i58

"""

class ComplexNumbers:

    #create your class here.

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def plus(self, other):

        self.real =  self.real+other.real
        self.imag = self.imag+other.imag

    def multiply(self, other):

        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        self.real = real_part
        self.imag = imag_part

    def print(self):
        print(f'{self.real} + i{self.imag}')

    def __str__(self):
        return f'{self.real} + i{self.imag}'



#Driver's code goes here.

c1  = ComplexNumbers(*map(int, input().split()))

c2 =  ComplexNumbers(*map(int, input().split()))

# Create the object


operation = int(input())

if operation == 1:
    c1.plus(c2)
    c1.print()

elif operation == 2:
    c1.multiply(c2)
    c1.print()



"""
Input Format:
4 5
6 7
2
"""