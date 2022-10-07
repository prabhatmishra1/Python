
#this is the linear approach
# def find_left_right_most(arr, key):
#     left_most = right_most = -1

#     for index, value in enumerate(arr):
        
#         #this for one time only 
#         if value == key and left_most == -1:
#             left_most = index
#         #this is for every time    
#         if value == key:
#             right_most = index
#     return left_most, right_most,

#Binary search approach
def find_left_right_most(arr, key):

    left_most = find_left_most_index(arr, key)
    right_most = find_right_most_index(arr, key)

    return left_most, right_most,

def find_left_most_index(arr, key):
    left_most = -1

    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == key:
            left_most = mid
            right = mid-1
        elif arr[mid] > key:
            right = mid-1
        elif arr[mid] < key:
            left = mid+1
    return left_most


def find_right_most_index(arr, key):
    right_most = -1
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == key:
            right_most = mid
            left = mid+1
        elif arr[mid] > key:
            right = mid-1
        elif arr[mid] < key:
            left = mid+1
    return right_most

if __name__ == "__main__":

    l = [0,0,1,1,2,2,2,2]
    output = find_left_right_most(l, 2)
    print(output)


