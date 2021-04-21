def Binary_Search(arr,item):
    l,u=0,len(arr)
    cnt=0
    while u>l:
        m=(l+u)//2
        if arr[m]==item:
            print(cnt)
            return m
        elif arr[m]>item:
            u=m-1
        else:
            l=m+1
        cnt+=1
    else:
        return -1                

if __name__=='__main__':
    arr=list(range(0,100000000000))
    item=999
    index=Binary_Search(arr,item)
    if index==-1:
        print("Element not found in the List")
    else:
        print("%d found at index %d"%(item,index))    