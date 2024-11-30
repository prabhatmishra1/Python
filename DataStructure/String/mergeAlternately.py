"""You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  abc
word2:  pqr
merged: apbqcr

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  ab
word2:  pqrs
merged: apbqrs
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  abcd
word2:    pq
merged: apbqcd
"""
# First Approach
def  mergeAlternately(word1, word2):
    """
    This approach is based on try and except
    """
    len_word1 = len(word1)
    output = list()
    for index in range(len_word1):
        try:
            output.append(word1[index])
            output.append(word2[index])
        except IndexError:
            output.append(word1[index+1::])
            break

    else:
        output.append(word2[index+1::])

    print("".join(output))

# Second Approach
def  mergeAlternately(word1, word2):
    """
    STEP-1: Get len of word1 and word2
    STEP-2: Get the min len
    STE-3: Iterate through min len
    STEP-4: Compare the remaining words and assign
    """
    len_word1 = len(word1)
    len_word2 = len(word2)
    min_len = min(len_word1, len_word2)
    output = list()
    for index in range(min_len):
        output.append(word1[index])
        output.append(word2[index])

    # if index < len_word1-1:
    #     output.append(word1[index+1::])

    # elif index < len_word2-1:
    #      output.append(word2[index+1::])
    # Append the remaining characters of the longer word
    output.append(word1[index+1::] if index < len_word1-1 else word2[index+1::] if index < len_word2-1 else "")

    print("".join(output))


# Third Approach
def  mergeAlternately(word1, word2):
    """
    This approach is based on string slicing
    """
    len_word1 = len(word1)
    output = list()
    for index in range(len_word1):
            output.append(word1[index] if word1[index:index+1] else "")
            output.append(word2[index] if word2[index:index+1] else "")
    else:
        output.append(word2[index+1::])

    print("".join(output))

if __name__ == "__main__":
    #TestCase: 1
    mergeAlternately("abc", "pqr")
    #TetCase: 2
    mergeAlternately("ab", "pqrs")
    #TetCase: 3
    mergeAlternately("abcd", "pq")


