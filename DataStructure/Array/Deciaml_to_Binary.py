#WAP to convert Decimal to binary

"""
First Approach(Use inbuilt bin method):
STEP-1: Using bin method

Second Approach(Use division method):
STEP-1: Using division method
STEP-2: Iterate and divide by 2 and keep the remainder in list
STEP-3: Convert that list to digit
STEP-4: Return the result

Third approach(Using bitwise operator)
STEP-1: Using bit 
"""

#First Approach
def convert_decimal_to_binary(decimal_number):

    return bin(decimal_number)[2:]
 
#Second Approach

def convert_list_to_digit(l):

    from functools import reduce

    return int(reduce(lambda a,b: str(a)+str(b), l))


def convert_decimal_to_binary(decimal_number):
        from collections import deque
        result = deque()
        while decimal_number:
            result.appendleft(decimal_number%2)
            decimal_number//=2
        return convert_list_to_digit(result)


def convert_decimal_to_binary(decimal_number):
        
        ans = i = 0
        while decimal_number != 0:
            bit = decimal_number & 1
            print(bit)
            ans = (bit*(10**i))+ans
            decimal_number = decimal_number>>1
            i+=1
        return ans

if __name__ == "__main__":
    decimal_number = 50
    output = convert_decimal_to_binary(decimal_number)
    print(output)





