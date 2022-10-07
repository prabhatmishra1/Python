"""
Input: nums = [2,4,1,1,6,5]
Output: 3
Explanation:
At index 0: There is no non-equal neighbor of 2 on the left, so index 0 is neither a hill nor a valley.
At index 1: The closest non-equal neighbors of 4 are 2 and 1. Since 4 > 2 and 4 > 1, index 1 is a hill. 
At index 2: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 2 is a valley.
At index 3: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 3 is a valley, but note that it is part of the same valley as index 2.
At index 4: The closest non-equal neighbors of 6 are 1 and 5. Since 6 > 1 and 6 > 5, index 4 is a hill.
At index 5: There is no non-equal neighbor of 5 on the right, so index 5 is neither a hill nor a valley. 
There are 3 hills and valleys so we return 3.
"""

def find_hills_valleys(arr):
    hill = 0
    valley = 0
    for index in range(1, len(arr)-1):
        neighbors = find_non_equal_neighbors(index, arr)
        print(neighbors)
        if neighbors[0] and neighbors[1]:
            value = arr[index]
            if value > neighbors[0] and value > neighbors[1] and value != arr[index-1]:
                hill+=1            
            elif value < neighbors[0] and value < neighbors[1] and  value != arr[index-1]:
                valley+= 1
    return (hill+valley)


def find_non_equal_neighbors(index, arr):
    value = arr[index]
    i = j = index
    left_neighbors = False
    right_neighbors = False
    #first look for left side
    while i > 0  or j <= len(arr)-1:
        #check left side
        if value != arr[i-1] and not left_neighbors:
            left_neighbors = arr[i-1]
        #check right side
        if value != arr[j+1] and not right_neighbors:
            right_neighbors = arr[j+1]  
        #check if we have found
        elif left_neighbors and right_neighbors:
            return left_neighbors, right_neighbors,
        elif not left_neighbors:
            i-=1
        elif not right_neighbors:
            j+=1
    return left_neighbors, right_neighbors,
        
if __name__ == "__main__":

    #arr = [2, 4, 1, 1, 6, 5]
    #arr = [1, 6, 5, 5, 4, 1]
    arr = [8, 2, 5, 7, 7, 2, 10, 3, 6, 2]
    #arr = [5,7,7,1,7]
    output = find_hills_valleys(arr)
    print(output)
