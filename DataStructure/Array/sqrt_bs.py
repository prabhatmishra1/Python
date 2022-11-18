#WAP to find sqrt of an number using binary search
def get_sqrt(n):
    left = 0
    right = n
    mid = n//2
    res = 0

    while left <= right:

        if(mid*mid>n):
            right = mid-1
        elif(mid*mid < n):
            res = mid
            left = mid+1
        elif(mid*mid == n):
            return mid
        mid = (left+right)//2
    return res


if __name__ == "__main__":

    n = 26
    output = get_sqrt(n)
    print(output)
