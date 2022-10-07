def sort_0_1_2(arr):

    i, j = 0, len(arr)-1
    k = j

    while i <= j:

        if arr[i] == 0:
            i += 1
        if arr[k] == 2:
            k -= 1
        #swap
        elif arr[i] == 1 and arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        
        #swap
        elif arr[j] == 2 and arr[k] == 1:
            arr[j], arr[k] = arr[k], arr[j]
            j -= 1
            k -= 1
    return arr


if __name__ == "__main__":
    arr = [0,1,2,2,1,0]
    output = sort_0_1_2(arr)
    print(output)
