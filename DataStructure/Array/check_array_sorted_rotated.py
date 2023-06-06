"""
Program to check weather array is rotated and sorted return True or False.
It means first array will be sorted then rotated
arr = [1,2,3,4,5]
arr = [2,3,4,5,1] k = 1  rotated and sorted
arr = [3,4,5,1,2] k = 2 rotated and sorted

Logic:
Yha per koi only one ek aisa pair hoga jo arr[i-1] < arr[i] ko justify krega
"""


def check_rotated_sorted(arr:list[int])-> bool:

    n = len(arr)
    count = 0
    for i in range(1, n-1,):
        if arr[i-1] > arr[i]:
            count+=1

    #do for first and last index

    if arr[n-1] >= arr[0]:
        count+=1

    return count==1


arr = [1,1,1]
print(check_rotated_sorted(arr))