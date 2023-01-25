
"""Given an integer array nums, move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


# method -1 

"""
pop zeros and extend in last of the same array
"""

# def move_zeros(arr):
    
#     zeros_count = 0
#     n = len(arr)
#     i = 0
#     while i < n:
#         if arr[i] == 0:
#             arr.pop(i)
#             zeros_count+=1
#             n-=1
#         else:
#             i+=1
#     #now extend the array to zeros list
#     print(arr)
#     arr.extend([0]*zeros_count)
#     return arr


# method -2

"""
Look at the problem in different way make non_zeros to left side.
How it works ?

Step-1: Traverse the array start from arr[i] to n
step-2: Keep one variable which will point the non zeros value index
Step-3: If arr[i]==0 then ignore
Step-4: If arr[i]=!0 swap(arr[i], arr[non_zeros])
Step-5: return the array
"""

def move_zeros(arr):
    non_zeros = 0   

    for i in range(len(arr)):     
        if arr[i]!=0:
            arr[i], arr[non_zeros] = arr[non_zeros], arr[i]
            non_zeros+=1

    return arr
if __name__ == "__main__":

    arr = [0,0,1]
    output = move_zeros(arr)
    print(output)


