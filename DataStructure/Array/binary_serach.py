def binary_search(arr, key):
    left = 0
    right = len(arr)-1

    while left <= right:
        m = (left+right)//2
        if arr[m] == key:
            return m
        elif arr[m] > key:
            right = m-1
        else:
            left = m+1


l = [6, 7, 10, 11, 15, 17, 20]
print(binary_search(l, 10))
