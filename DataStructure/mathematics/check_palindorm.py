"""
Check the given the digit is palindrom or not

for example: 1221 its a palindrom number
123 = Its not an palindrom number
"""


class Solution:

    #First approach to solve with mathematical approach
    def check_palindrom_number(self, digits):

        rev = 0
        digits_copy = digits
        while digits:
            rem = digits%10  #It will give the last digit
            rev = rev*10+rem # It will get reverse of the digit
            digits//=10 #It will trim the last digit

        return "Plaindrom" if rev == digits_copy else "Not Plaindrom"


    #Second approach using string slicing
    def check_palindrom_number_str(self, digits):
        digit_str = str(digits)
        # just reverse the string and check
        return "Plaindrom" if digit_str == digit_str[::-1] else "Not Plaindrom"



if __name__ == "__main__":

    digits = 1021

    solution = Solution()

    output = solution.check_palindrom_number(digits)

    print(output)

    output = solution.check_palindrom_number_str(digits)

    print(output)


