def Modified_Bubble_Sort(arr,n):
    already_sorted=True
    for rond in range(1,n):
        for i in range(n-rond):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                already_sorted=False
        if already_sorted:
          break
    return arr
        



if __name__ == '__main__':
    arr=Modified_Bubble_Sort([1,2,3,4],len([1,2,4,3]))
    print(arr)
