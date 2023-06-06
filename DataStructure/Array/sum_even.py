#WAP to find sum of N even number

"""
First Approach O(n):
We can do this using loop.

Second Approach O(1):
We can do this using formula n * (n + 1)
"""

# First Approach
def get_even_sum(n):
    total_sum = 0
    while n:
        if (n%2==0):
            total_sum+=n
        n-=1
    return total_sum

#Second Approach:

def get_even_sum(n):

    return (n // 2) * ((n // 2) + 1)

if __name__ == "__main__":

    # 1,2,3,4,5,6   
    output = get_even_sum(8)
    print(output)


