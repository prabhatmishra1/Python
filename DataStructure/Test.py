
def bubble_sort(arr):
    n = len(arr)-1
    for round_  in range(n-1):

        for i in range(0, n-round_):

            #swap
            if arr[i] > arr[i+1]:
                arr[i] , arr[i+1] = arr[i+1], arr[i]
    
    return arr


if __name__ == "__main__":

    arr = [2,3,5,1,4]

    output =  bubble_sort(arr)
    print(output)