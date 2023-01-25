"""Reverse subpart of array
"""

#method-1
# def reverse_sub_array(arr, m):
#     n = len(arr)
#     slice_arr = arr[m+1:n]
#     arr[m+1:n] = slice_arr[::-1] #reverse arr
#     return arr


def reverse_sub_array(arr, m):
    n = len(arr)
    _round = (n-(m+1))//2
    j = n-1
    i = m+1
    while i <= j:
        temp = arr[j]
        arr[j] = arr[i] 
        arr[i] = temp
        i+=1
        j-=1
    return arr  
if __name__ == "__main__":
    arr = [10,4,5,2,3,6,1,3,6]
    arr = [1,4,5,6,6,7,7]
    #arr = [1,2,3,4,5,6]

    #10 4 5 2 6 3 1 6 3
    m = 3
    output = reverse_sub_array(arr, m)
    print(output)


