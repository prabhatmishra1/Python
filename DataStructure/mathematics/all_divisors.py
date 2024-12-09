"""
Write a python script to get all divisors of a number.

Example: Number = 15
Divisors are  = 1, 3, 5, 15

Example: Number = 20
Divisors are: 1, 2, 4, 5, 10, 20
"""


class GetDivisors:

    def __init__(self, n):
        self.n = n
        self.result = []

    def get_all_divisor_naive_approach(self):
        """
        So in this we will run the loop from 1 to n and we will check,
        If value of loop is dividing the number then it will divisor
        else continue
        """
        for value in range(1, self.n+1):

            if self.n % value == 0:
                self.result.append(value)

        return self.result

    def get_all_divisor_sqrt_approach(self):
        """
        So in this approach will run the loop from 1 to sqrt(n)
        and so it reduce the loop and the we will check the multiple
        """
        from math import sqrt
        for value in range(1, int(sqrt(self.n))+1):

            if self.n % value == 0:
                self.result.append(value)

                if  n//value != value:
                    self.result.append(n//value)


        return self.result



if __name__ == "__main__":
    n = 36
    divisors =  GetDivisors(n)
    # print(divisors.get_all_divisor_naive_approach())
    print(divisors.get_all_divisor_sqrt_approach())
