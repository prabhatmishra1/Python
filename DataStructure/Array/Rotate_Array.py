"""
Actually Rotate Array is very famous question and can done various ways.

What Array Rotation ?

It means shifting the element k times

for e.g = [2,1,4,5,6]

What left Rotations ?
It means traversal will start from left and move to right

What right Rotations ?
It means traversal will start from right and move to left

Rotate left 1 times: [1,4,5,6,2] index start will form 0
Rotate left 2 times: [4,5,6,2,1]

Rotate right 1 times: [6,2,1,4,5,] index start will n-1(last index se)
Rotate right 2 times: [5,6,2,1,4,]
Rotate right 3 times: [4,5,6,2,1]
"""



#method 1
# "swapping from left to right"

# def rotate_array(arr, k):
#     n = len(arr)
#     for i in range(k):
#         for j in range(n-1):
#             arr[j], arr[j+1] =  arr[j+1], arr[j] 
#     return arr


# "using mod formula"
# def rotate_array(arr, k):
#     n = len(arr)
#     temp_array  = arr.copy()
#     [arr[(i+k)%n]  for i in range(n)]
#     for i in range(n):
#         temp_array[(i+k)%n] = arr[i]
#     arr = temp_array
#     return arr

"using list slice"
# def rotate_array(nums, k):
#     k = k % len(nums)
#     if k > 0:
# 	    nums[:k], nums[k:] = nums[-k:], nums[:-k]
#     return nums

"using deque"

def rotate_array(nums, k):
    from collections import deque

    de =  deque(nums)
    de.rotate(-k)
    return list(de)

if __name__ == "__main__":

    arr = [1,2,3,4,5]
    print(rotate_array(arr, k=2))

