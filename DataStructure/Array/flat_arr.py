# output list
output = []

# function used for removing nested
# lists in python using recursion


def removeNestings(l):
    for i in l:
        if isinstance(i, list):
            removeNestings(i)
        else:
            output.append(i)




        



if __name__ == "__main__":
    
    l = [[[2],[3, [4, [5]]]],1,[4,]]

    reemovNestings(l)
    print(output)
