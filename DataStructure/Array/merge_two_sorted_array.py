def merge_two_sorted_array(arr1, arr2):
    i = j = 0
    arr1_size = len(arr1)
    arr2_size = len(arr2)
    sorted_arr = list()
    while j <  arr2_size and i < arr1_size:
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i+=1
        else:
            sorted_arr.append(arr2[j])
            j+=1
    if i < arr1_size:
        sorted_arr.extend(arr1[i::])
    if j < arr2_size:
        sorted_arr.extend(arr2[j::])
    
    result = get_array_median(sorted_arr)
    return result

def get_array_median(arr):
    index = len(arr)//2

    if len(arr)%2!=0:
        return arr[index]
    else:
        return (arr[index-1]+arr[index])/2

if __name__ == "__main__":

    arr1 = [1, 2]
    arr2 = [3, 4]
    output = merge_two_sorted_array(arr1, arr2)
    print(output)


    

