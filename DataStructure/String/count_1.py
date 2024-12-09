"""
You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1".
What is the length of the longest substring achievable that contains only "1"?
For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.
"""
def count_the_longest_substring(string):
    index = 0
    flipped_string = list()
    for char in string:
        if char == "0":
            flipped_string_1 = string[:index:]+'1'+string[index+1::]
            flipped_string.append(flipped_string_1)

        index+=1

    max_ = 0
    cnt = 0
    for string in flipped_string:
        cnt = len(max([value for value in string.split('0') if '1' in value]))
        if max_ < cnt:
            max_ = cnt
    return  max_






if __name__ == "__main__":

    input = "10101111"
    print(count_the_longest_substring(input))


# [1111100111, 1101110111, 1101101111]
