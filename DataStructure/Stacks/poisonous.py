def poisonous_stack(arr):
    s = set()
    res = list()
    for i in range(1, len(arr)):
        for j in range(1, len(arr)):
            try:
                if arr[j] > arr[i-1]:
                    arr.remove(arr[j])
                    s.add(i)
            except:
                pass
    print(len(s))
    print(s)

arr = [6,5,8,4,7,10,9]

if __name__ == "__main__":
    poisonous_stack(arr)
