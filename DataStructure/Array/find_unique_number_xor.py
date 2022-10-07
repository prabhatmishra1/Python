from functools import reduce
def find_unique(arr):
    return reduce(lambda total,value: total^value, arr)

if __name__ == "__main__":

    output = find_unique([1,1,1,2,2,3])
    print(output)
