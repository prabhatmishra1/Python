def sort_0_1(arr):

    i, j = 0, len(arr)-1

    while i<=j:

        if arr[i]==0:
            i+=1
        elif arr[j]==1:
            j-=1
        #swap
        elif arr[i]==1 and arr[j]==0:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1  
    return arr


if __name__ == "__main__":
    arr = [0,0,1,0,1,0]
    output = sort_0_1(arr)
    print(output)




