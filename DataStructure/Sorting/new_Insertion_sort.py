def insertion_sort(arr):
    for rond in range(1,len(arr)):
        temp=arr[rond]
        i=rond-1
        while i>=0 and temp<arr[i]:
              arr[i+1]=arr[i]
              i=i-1
        arr[i+1]=temp      
    return arr


if __name__=="__main__":
    arr=insertion_sort([6,10,4,3,2,1])
    print(arr)
