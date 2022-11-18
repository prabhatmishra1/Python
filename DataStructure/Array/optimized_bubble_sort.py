"""
So normal bubble sort takes O(n^2) time because it traverse(inner loop) entire array 
even though array is sorted.
We can avoid this once we will come to know that our array got sorted we do not need 
to loop through entire round and using this the best case will for binary search O(n).
=====================================================================================
How it works ?
STEP-1: we have to keep an eye that when our array got sorted
STEP-2: The idea is when swapping in not happing it means array is sorted only
STEP-3: Once you know swapping is not happing break the inner loop
STEP-4 Keep on flag variable(swapped=False) which will tell us about array swapping
"""


def optimized_bubble_sort(arr):
    n = len(arr)
    for _round in range(n-1): #bcz last value will get sorted auto only
        print("Round-{}".format(_round+1))
        swapped = False
        for i in range(n-_round-1):
            print(arr)
            if arr[i] > arr[i+1]:
                #swapping
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr
if __name__ == "__main__":
    arr = [15,4,100,500]
    output  = optimized_bubble_sort(arr)
    print(output)
