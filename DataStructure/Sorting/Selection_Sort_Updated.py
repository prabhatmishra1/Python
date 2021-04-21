def Selection_Sort(arr,n):
    for i in range(n-1):
        loc=MIN(arr,n,i)
        arr[i],arr[loc]=arr[loc],arr[i]
    return arr    




def MIN(arr,n,start):
    m=arr[start]
    index=0
    for i in range(start,n):
        if arr[i]<=m:
            m=arr[i]
            index=i
    print(index)        
    return index


if __name__== '__main__':
    arr=Selection_Sort([34,11,67,8,13],len([34,11,67,8,13]))
    print(arr)
