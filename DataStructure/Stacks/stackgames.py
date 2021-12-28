def twoStack(maxSum,a,b):

    n = len(a) if a < b else len(b)
    i = 0
    j = 0
    s = 0
    cnt = 0
    while n and (s < maxSum) :

        if a[i] < b[j]:
            print(a[i])
            s = s+a[i]
            i = i+1
        else:
            print(b[j])
            s = s+b[j]
            j = j+1
        cnt+=1
        n-=1
    return cnt

if __name__ == "__main__":

    a = [1,2,3,4,5]
    b = [6,7,8,9]
    maxSum = 10

    res = twoStack(maxSum,a,b)
    print("result",res)