def intersection_sorted_array(arr1, arr2):
    max_len = max(len(arr1), len(arr2))
    i = 0
    j = 0
    intersection = []
    while i <= len(arr1)-1:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            i += 1
            j += 1
        elif arr2[j] < arr1[i]:
            j += 1
    return intersection

if __name__ == "__main__":

    arr1 = [3]
    arr2 = [6]
    output = intersection_sorted_array(arr1, arr2)
    print(output)
