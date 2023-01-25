"""
Insertion sort is also very famous sorting technique which take O(n^2)

How it works ?

Explanation:
Lets understand by this example if someone gives you currency in random order
and told you to keep the currency in sorted order then how you will do that? the idea is 
every time you have to check the proper place for the current note and then you will put.
The same way you need to sort the value in insertion sort

STEP-1: Start outer loop(i) form 1 to n
STEP-2: Start inner loop(j) until from j > 0 and and arr[j] < arr[j-1]
STEP-3: Return the arr
"""

def insertion_sort(arr):
    for _round in range(1, len(arr)):
        j = _round
        temp = arr[j]

        while j > 0 :
            if temp < arr[j-1]:
                arr[j-1] = arr[j]
            j-=1
        arr[j-1] = temp
    return arr


if __name__ == "__main__":

    arr = [12, 6]

    output  =  insertion_sort(arr)
    print(output)
