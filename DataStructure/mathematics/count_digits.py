"""
Count the number of the digits
For e.g 48745
count  = 5
"""


class Solution:

    def count_the_digits_using_loop(self, digits):
        # if you divide the number by 10 your last digit will be removed
        count = 0
        while digits:
            digits = digits//10
            count+=1

        return count






if __name__ == "__main__":

    digits = 12345
    solution =  Solution()
    output = solution.count_the_digits_using_loop(digits)
    print(output)