"""
Write a program to calculate the HCF(GCD) of two number:

HCF = Highest common Factor
GCD = Grates common Divisor

12 and 18:
Divisors of 12 are 1, 2, 3, 4, 6 and 12
Divisors of 18 are 1, 3, 6, 9 and 18
The common Divisors are 1, 3 and 6. The greatest common divisor or GCD is 6
"""

class Solution:

    #First approach using loop
    def calculate_hcf(self, a, b):
        #get min value first
        min_value = a if a < b else b

        for value in range(min_value, 0, -1):

            if a%value == 0 and b%value == 0:
                    break

        return value
    # Using euclidean algorithm
    def calculate_hcf_using_euclidean(self, a, b):
        """
        STEP-1: Get the value a and b
        STEP-2: Get grater value in a and b
        STEP-3: Divide the grater value by smaller value and take the reminder
        STEP-4: Now divide the smaller value by reminder
        STEP-5 Repeat until the reminder the is 0
        """
        while a != b:
            if  a > b:
                a = a-b
            else:
                b = b-a
        return a

    def calculate_hcf_using_recursion(self, a, b):

        if b == 0:
            return a
        return self.calculate_hcf_using_recursion(b, a%b)

    def calculate_hcf_using_math_module(self, a, b):
        """
        In python math module we already have gcd method which take list of arguments
        and return the result in float
        """
        from math import gcd

        return gcd(a, b)


if __name__ == "__main__":

    a, b = 36, 9

    solution = Solution()
    print(solution.calculate_hcf(a, b))

    print(solution.calculate_hcf_using_euclidean(a, b))

    print(solution.calculate_hcf_using_recursion(a, b))

    print(solution.calculate_hcf_using_math_module(a, b))





