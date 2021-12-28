def sort_dict_by_key(d):
    key_arr = list(d.keys())
    n = len(key_arr)
    for  i in range(1,n):
        for j in range(n-i):
            if key_arr[j] > key_arr[j+1]:
                key_arr[j],key_arr[j+1] = key_arr[j+1], key_arr[j]

    return { key:d[key] for key in key_arr }


if __name__ == "__main__":
  d = {'a':12, 'c': 34, 'b': 40, 'f': 90}
#   d = [34,15,6,9]
  res = sort_dict_by_key(d)
  print(res)
