def largest_area(arr):
    n = len(arr)
    for i in range(n):
        left = i
        right = i

        # take right most index
        while right<n-1 and arr[i]<arr[right+1]:
            right+=1
        # print("{}->{} = {}".format(i,arr[i],right))

        while left > 0 and arr[left-1]>arr[i]:
            left-=1

        # print("{}->{} = {}".format(i,arr[i],left))
        area = (right-left+1)*arr[i]
        print(area)




if __name__ == "__main__":
    l = [2,1,5,6,3,4]
    largest_area(l)
