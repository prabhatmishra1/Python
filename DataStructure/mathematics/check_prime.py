"""
Write a python program to check a number is prime or not ?

Solution:

What is Prime number:

A number which can divisible by itself or 1

Example: 2, 11, 13, 17,

Note: 2 only one even prime number others all are odd numbers

Note: -1, 0, 1 is not an prime number

Note: All prime number are grater then 1 Example Prime number start with 2......


First Approach:

We can check the divisibility from 1 to N and if if any number divide except itself or 1
then its not a prime number otherwise it will be a prime number

Second Approach:
Now we know if N is large number then it will more time to check in that can case we can
calculate the square root on N and then check prime number, so it will reduce the check

Note: If a number N>3 and N>3 is divisible by either 2 or 3, it cannot be a prime because it has additional divisors (2 or 3).
Note: If a number N is divisible by 2  or 3 then its not a prime number
"""


class Solution:

    # First approach naive approach using loop
    def check_prime(self, n):
        if n == 1:
            return False
        res = True
        for value in range(n-1, 1, -1):
            if n%value == 0:
                res = False
                break
        return res

    #Second approach with
    def check_prime_with_sqrt(self, n):
        from math import sqrt
        # handel the edge case first
        if n <=1:
            return False

        #range of 2 to 3
        if n<=3:
            return True

        if n%2 == 0 or  n%3 == 0:
            return False

        for number in range (5, int(sqrt(n))):

            if n % number == 0:
                return False
        else:
            return True

    def check_prime_6k(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:  # Only check divisors up to sqrt(n)
            if n % i == 0 or n % (i + 2) == 0:  # Check multiples of 6k ± 1
                return False
            i += 6
        return True





# Drive code

if __name__ == "__main__":
    n = 61
    solution = Solution()
    print(solution.check_prime(n))
    print(solution.check_prime_with_sqrt(n))
    print(solution.check_prime_6k(n))
