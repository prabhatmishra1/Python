"""
So convert the list [1,2,3,4] to digits 1234
"""



class Solution:

    #First approach
    def convert_list_to_digit(self, list_data):
        """
        So this is the concept of place value
        """
        result = 0
        for value in list_data:
            result=result*10+value

        return result
    # convert them into str and map to int
    def convert_list_to_digit_by_str(self, list_data):
        """
        So this is the concept of place value
        """
        return "".join(map(str, list_data))



if __name__ == "__main__":
    data = [0, 1, 0, 2, 3, 0, 0]
    solution =  Solution()

    output = solution.convert_list_to_digit(data)
    print(output)

    output = solution.convert_list_to_digit_by_str(data)
    print(output)