#WAP to find sum of N number
"""
Like N=5 then result = (1+2+3+4+5)
"""
"""
First Approach O(n):
----------------
STEP-1: We can solve this using loop
STEP-2: I will take O(n) time

Second Approach O(1):
----------------
STEP-1: We can solve this using one formula n/2(a+l)
The summation formula you mentioned, n/2(a + l), is used to calculate the sum of an
arithmetic series, where "n" represents the number of terms in the series, 
"a" is the first term, and "l" is the last term.

STEP-2:  Like N=5 [1,2,3,4,5]
Where a = 1, n = 5 , l = 5

STEP-3 It will take O(1)
"""


# def get_sum(n):
#     total_sum = 0
#     while n:
#         total_sum+=n
#         n-=1
#     return total_sum

def get_sum(n):
    "use summation formula"
    a = 2
    l = n
    return  n/2*(a+l)

if __name__ == "__main__":

    output = get_sum(5)
    print("Output", output)
     



