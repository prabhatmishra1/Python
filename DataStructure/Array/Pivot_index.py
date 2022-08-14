def find_pivot_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    right_sum = total_sum
    for i in range(len(arr)):
        right_sum = right_sum-arr[i]
        if left_sum == right_sum:
            return i
        else:
            left_sum = left_sum+arr[i]
    else:
        return -1

l = [1, 7, 3, 6, 5, 6]
print(find_pivot_index(l))
