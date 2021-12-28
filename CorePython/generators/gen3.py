def add(arr):
    mx = -1
    mi = 1000
    for i in range(len(arr)):
        s = 0
        for j in range(len(arr)):

            if not j==i:
               print(arr[j],end= ' ')
               s = s+arr[j]
        print("sum=", s)
        print()
        if mx < s:
            mx = s
        if mi > s:
            mi = s
    print("max = %d  min = %d"%(mx,mi))

if __name__ == "__main__":
    add([1,2,3,4,5])
