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

    l =  [1,2,3,[4,5,[6,7,8,[13,14]],9,10],11,12]

    removeNestings(l)
    print(output)
