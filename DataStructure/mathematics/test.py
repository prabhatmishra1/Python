# 1 1 2, 3, 5, 8, 13


def fib(start, end):

    if start != end:
        res = fib(start+1, end) + fib(start+1, end+1)
        print(res)

    return

    # @property
    # request.data()



if __name__  == "__main__":

    # end = 10
    # fib(1, end)

    a = 10
    b = 20
    b = a
    a = 5
    # print(a, b)

    # b = 20
    # a = 5

    l = [1,2,3,4,5, [1,2,3]]

    other = l.copy()

    other[5][0] = 20

    print(other)
    print(l)