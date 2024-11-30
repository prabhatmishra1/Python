"""
Write a python program to calculate the LCM of two numbers

LCM: Least Common Multiple


Example: Multiple of 3 are: 3, 6, 9, 12, 15 ..........

Now let say two numbers are given
a = 4
b = 6

Multiple of a: 4, 8, 12, 16, 20, 24, 28, 36, 40

Multiple of b: 6, 12, 18, 24, 30, 36, 42, 48, 54, 60

Common: 12, 24, 36....

Lest Common: 12


Logic part:
1  will the least LCM of any number and a*b will be max LCM so in that case our range will be

(1, a*b) in this range only multiple will be there
"""

class Solution:

    #First approach using loop
    def calculate_lcm(self, a, b):

        for value in range(1, a*b):

            if  value % a == 0 and  value % b == 0:
                break

        return value

    def get_gcd(self, a, b):
        if b==0:
            return a
        return self.get_gcd(b, a%b)

    #Second approach using recursion
    def calculate_lcm_using_gcd(self, a, b):
        return a*b // self.get_gcd(a, b)







if __name__ == "__main__":

    solution = Solution()
    a , b = 4, 6
    print(solution.calculate_lcm(a,b))
    print(solution.calculate_lcm_using_gcd(a, b))




