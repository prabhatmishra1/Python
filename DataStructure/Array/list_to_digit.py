#WAP to make digit for list

#Example [1,2,3,4]=> 1234

"""
First Approach O(n):
STEP-1: Convert this list to string and concatenate them
STEP-2: Start loop for n times and convert them into string
STEP-3: Concatenate one by one   
Note-:  This approach will only work for integer values not for integer 

Second Approach O(n):
We can apply some maths and we can solve this
STEP-1: Start loop for n times
STEP-2: We have add the place value every time and we can do this
STEP-3  Formula=> result = (result*10)+value
                where:
                result = 0
                value = very loop digit
STEP-4: 
"""

def convert_list_to_digit(l):

    from functools import reduce

    return int(reduce(lambda a,b: str(a)+str(b), l))


def convert_list_to_digit(l):
    result = 0
    for value in l:
        result = (result*10)+value
    return result
if __name__ == "__main__":

    l = [1,2,3,4.2]

    output = convert_list_to_digit(l)
    print(output)
