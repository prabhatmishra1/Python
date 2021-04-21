def Bubble_Sort(arr,n):
    for rond in range(1,n):
        for i in range(n-rond):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
        



if __name__ == '__main__':
    n=Bubble_Sort([34,15,29,8],len([34,15,29,8]))
    print(n)
