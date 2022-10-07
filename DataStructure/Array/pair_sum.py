def pair_sum(arr, s):
    pair_sum_list = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+ arr[j] == s:
                pair_sum_list.append((arr[i], arr[j]))

    s = pair_sum_list.sort(key=lambda y: y[0])
    print(pair_sum_list)
    return pair_sum_list.sort(key=lambda y: y[0])


if __name__ == "__main__":

    output = pair_sum([2,-3,3,3,-2], 0)
    print(output)
