'''def linear_search(arr,n=None):
    i=0
    while i <len(arr):
        if arr[i]==n:
            print("%d found at index %d" %(n,i))
            break
        i+=1    
    else:
        print("Element not found in the list.")    

'''

def linear_search(arr,n=None):

    for index, value in enumerate(arr):
        if n==value:
            print("%d found at index %d" %(n,index))
            break
    else:
        print("Element not found in the list.")




if __name__=="__main__":
    arr=[15,5,20,35,2,42,67,17]
    linear_search(arr,n=17)