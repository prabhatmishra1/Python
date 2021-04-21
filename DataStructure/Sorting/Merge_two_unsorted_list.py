def mergesort(arr):
    if len(arr)<=1:
      return #if size of array is 1 let not do any thing

    #finding the mid of array
    mid=len(arr)//2
    arr1=arr[:mid]
    arr2=arr[mid:]

    mergesort(arr1)# it will return soreted left array
    mergesort(arr2)# it will return soreted right array
    merge_two_sorted_list(arr1,arr2,arr)
      
    


#merge two sorted array
def merge_two_sorted_list(arr1,arr2,arr):
    i=j=k=0
    len_a=len(arr1)
    len_b=len(arr2)
    while i<len_a and j<len_b:
        if arr1[i]>arr2[j]:
            arr[k]=arr2[j]
            j+=1
        else:
            arr[k]=arr1[i]
            i+=1
        k+=1    
    while i<len_a:
        arr[k]=arr1[i]
        i+=1
        k+=1

    while j<len_b:
       arr[k]=arr2[j]
       j+=1
       k+=1    

if __name__ == "__main__":
    arr=[10,9,5,6,3,4,11,18]
    mergesort(arr)
    print(arr)
