def merge_two_sorted_list(arr1, arr2):
    n =       len(arr1) if len(arr1)>=len(arr2) else len(arr2)
    res = []
    i, j = 0, 0
    while n:
        if i < len(arr1) and arr1[i] < arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
        n-=1
    if i != len(arr1):
       res.extend(arr1[i:])
    else:
        res.extend(arr2[j:])
    return res

if __name__ == "__main__":
    l1 = [1,5,6,7,8]
    l2 = [6,7]
    res=merge_two_sorted_list(l1,l2)
    print(res)

