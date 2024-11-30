"""
Write a python script to get the prime factorization of a number

What is prime factorization?

Prime factorization involves breaking down a number into its prime number components. For example, the prime factors of 100 are 2 and 5. Here's how you get there:

Divide 100 by 2 (the smallest prime number) to get 50.
Divide 50 by 2 to get 25 (2 occurrences of 2).
Divide 25 by 5 to get 5.
Divide 5 by 5 to get 1 (2 occurrences of 5).
So, the prime factorization of 100 is 2*2*5*2.


Solutions:

First Approach:

So first approach will be naive approach where will start the loop from 2 to N

STEP-1: Run loop from 1 to N
STEP-2: Check if the N is divisible by value
STEP-3: Store the value in the and update the N = N//value
STEP-4: If not then increment the value of
"""



class PrimeFactorization:
    """
    This class will return prime factorization of a number
    """

    def __init__(self, number):
        self.number = number
        self.result = []

    # First Approach
    def get_prime_factorization_naive_approach(self):
        """
        So first approach will be naive approach where will start the loop from 2 to N
        STEP-1: Run loop from 1 to N
        STEP-2: Check if the N is divisible by value
        STEP-3: Store the value in the and update the N = N//value
        STEP-4: If not then increment the value
        """

        value = 2
        n = self.number
        while value < n:
            # check if it is fully divisible
            if n%value == 0:
                self.result.append(value)
                n = n//value
            else:
                value+=1
        return self.result

    @staticmethod
    def check_prime(n):
        """
        Check number is prime or not?
        """
        from math import sqrt
        if n == 1:
            return False

        if n == 2:
            return True

        for number in range(2, int(sqrt(n))):

            if n % number == 0:
                return False

        return True



    def get_prime_factorization_by_checking_prime_number(self):
        """
        We need a function that takes a number and prints its prime factors.
        We'll run a loop from 2 to the number itself and check two things for each number:
        1. Is it a prime number?
        2. Does it divide the given number?
        """

        value = 2
        n = self.number
        while value < n:
            # check if it is fully divisible
            if self.check_prime(value) and n % value == 0:
                self.result.append(value)
                n = n//value
            else:
                value+=1
        return self.result




if __name__ == "__main__":
    n = 36
    prime_factor =  PrimeFactorization(n)

    # print(prime_factor.get_prime_factorization_naive_approach())
    print(prime_factor.get_prime_factorization_by_checking_prime_number())


