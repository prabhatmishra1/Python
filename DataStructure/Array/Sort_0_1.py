"""
Sort 0 and 1 can be solved using binary search approach.
How it works ?
STEP:1- Take two pointer i and j where i will start from 0 and j will point to 
last index.
STEP:2- This is two pointer approach where i and j will travel i->[]<-j.
STEP:3- If arr[i] has 0 increment i 
STEP:4- if arr[j] has 1 increment j
STEP:5 If arr[i]== 1 and arr[j] == 0 it means we need to swap them and increment both.
"""

def sort_0_1(arr):

    i, j = 0, len(arr)-1

    while i<=j:

        if arr[i]==0:
            i+=1
        elif arr[j]==1:
            j-=1
        #swap
        elif arr[i]==1 and arr[j]==0:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1  
    return arr


if __name__ == "__main__":
    arr = [0,0,1,0,1,0]
    output = sort_0_1(arr)
    print(output)




