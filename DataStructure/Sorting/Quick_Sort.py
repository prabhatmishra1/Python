# def Swap(a,start,end):
#    print(a)
#    if start != end: 
#         temp=a[start]
#         a[start]=a[end]
#         a[end]=temp

# def Partition(arr,start,end):
#     pivot_index=0
#     pivot=arr[pivot_index]
#     while start<end:
#         while start < len(arr) and arr[start] <= pivot:
#             start+=1
#         while arr[end]>pivot:
#             end-=1
#         if start<end:    
#            Swap(arr,start,end)

#     Swap(arr,pivot_index, end)    
#     return end

# def Quick_Sort(arr,start,end):
#     if start < end:
#         loc=Partition(arr,start,end)
#         Quick_Sort(arr,start,loc-1)#Left parition
#         Quick_Sort(arr,loc+1,end)#Right partition



# if __name__=='__main__':

#     arr=[35,20,15,25,80,50,90,45]

#     Quick_Sort(arr,0,len(arr)-1)

#     print(arr)



################################################################



# implementation of quick sort in python using hoare partition scheme

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')






