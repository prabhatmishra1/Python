"""
So we have string given and but we have to print in different way

Input: "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
Output:  A CD FGH JKLM OPQRS UVWXYZ
"""


class Solution:

    def custom_grouping(self, s):
        # Split the string into individual letters
        letters = list(s)

        # Define the grouping pattern
        group_sizes = [1, 2, 3, 4, 5, 6]

        # Initialize variables
        output = []
        index = 0

        # Loop through the group sizes and build each group
        for size in group_sizes:
            group = ''.join(letters[index:index + size])
            output.append(group)
            index += size+1

        # Join the groups with spaces and return the result
        return ' '.join(output)


if __name__ == '__main__':
    # Test the function
    input_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    solution = Solution()
    output_str = solution.custom_grouping(input_str)
    print(output_str)