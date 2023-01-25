"""
Selection sort is also very famous sorting algorithm which takes O(n^2) for worst 
case.

How it works ?

STEP-1: Traverse array from 0 to n 
STEP-2: Find min value in arr[1-n] and swap with i-th index
STEP-3  Repeat the step-2 and array will be sorted
"""
def selection_sort(arr):
    n = len(arr)
    for index in range(n-1):
        min_index = index
        for i in range(index+1, n):
            if arr[min_index] > arr[i]:
                min_value = arr[i]
                min_index = i
        #swap min_value to index value
        arr[index], arr[min_index] = arr[min_index], arr[index]
    return arr

if __name__ == "__main__":

    arr = [1, 19, 10, 0, 4, 8, 3]

    output = selection_sort(arr)
    print(output)



