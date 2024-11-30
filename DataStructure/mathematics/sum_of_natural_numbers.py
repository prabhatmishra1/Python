"""
Find the sum of natural number for e.g: 1+2+3+4+5

So n will be given and you need to calculate the natural numbers
"""



class Solution:

    # First approach will be solve this problem using loop
    def calculate_the_sum_of_natural_number(self, n):

        res = 0
        for number in range(1, n+1):
            res += number

        return res

    # Using  python generative
    def calculate_the_sum_of_natural_number_by_generator(self, n):

        res = 0
        for number in range(1, n+1):

            yield  number

    # Using python reduce
    def calculate_the_sum_of_natural_number_by_reduce(self, n):
        from functools import reduce
        return reduce(lambda x, y: x+y, list(range(1, n+1)))

    # Using math formula
    def calculate_the_sum_of_natural_number_by_formula(self, n):

        return (n*(n+1))//2






if __name__ == "__main__":

    n=10
    solution = Solution()
    output = solution.calculate_the_sum_of_natural_number(n)
    print(output)

    output = solution.calculate_the_sum_of_natural_number_by_generator(n)
    print(sum(output))

    output = solution.calculate_the_sum_of_natural_number_by_reduce(n)
    print(output)

    output = solution.calculate_the_sum_of_natural_number_by_formula(n)
    print(output)

