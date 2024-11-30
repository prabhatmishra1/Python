"""
Now we have to find the string count with sequence manner.
For Example: aabccccaaabb
Output: a2b1c4a3b2
Explanation: So you can see that we are not calculating the frequency of strings we calculating in
sequence manner like aa = 1 , b=1, cccc=4, aaa=3, bb=2

Other Example: abcd
Output: a1b1c1d1

Write a program to achieve this.
"""

class Solution:

    # First approach:
    """
    We solve this problem using two loop outer loop will take one char and inner loop will run until
    we are getting the match else move to next step

    Time Complexity O(n^2)
    """
    def find_sequence_count(self, string):
        """
        STEP-1: Get len of string
        STEP-2: Run the loop from step
        STEP-3: Check the value with inner loop
        STEP-4: Keep the data in list and keep on updating
        STE-5: Join the string and return
        """
        i = 0
        j = 1
        len_string = len(string)
        count = 1
        result = []

        while i < len_string:
            if j < len_string and string[i] == string[j]:
                j+=1
                count+=1

            else:
                result.append(f'{string[i]}{count}')
                i = j
                j = i+1
                count = 1
        else:
           return "".join(result)




if __name__ == "__main__":

    solution = Solution()
    print(solution.find_sequence_count("aabccccaaabb"))


