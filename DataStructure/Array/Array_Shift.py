def left_rotate(arr,n):
    while n:
        temp=arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]      
        arr[i+1]=temp
        n-=1
arr=[1,2,3,4,5]
left_rotate(arr,1)
print(arr)