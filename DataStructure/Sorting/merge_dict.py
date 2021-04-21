def mergeSort(elements, key=None,descending=False):
    if len(elements)<=1:
        return

    mid=len(elements)//2 
    left=elements[:mid]
    right=elements[mid:]
    mergeSort(left,key,descending)
    mergeSort(right,key,descending)
    merge_two_sorted_list(elements,left,right,key,descending)

def merge_two_sorted_list(elements,left,right,key,descending):
    i=j=k=0
    if not descending:
        while i<len(left) and j<len(right):
            if left[i][key] < right[j][key]:
                elements[k]=left[i]
                i+=1
            else:
                elements[k]=right[j]
                j+=1 
            k+=1
    if descending:
        while i<len(left) and j<len(right):
            if left[i][key] > right[j][key]:
                elements[k]=left[i]
                i+=1
            else:
                elements[k]=right[j]
                j+=1 
            k+=1


    while i<len(left):
          elements[k]=left[i]
          i+=1
          k+=1
    while j<len(right): 
        elements=right[j]
        j+=1
        k+=1    

elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]


mergeSort(elements,key='name')

print(elements)
