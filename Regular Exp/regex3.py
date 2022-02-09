'''Q. Write a Python Program to check whether the given mail id is
valid gmail id or not?
'''
import re
import math

def check_email(value):

    s = re.fullmatch('[a-zA-Z0-9_.]*@[gamilyahoothecode]*.com', value)
    print(s)

    if  s:
        return True
    return False


def check_float(value):
    # [+-]?[0-9]*.{1}[0-9]+
    flag = False
    res = re.fullmatch('[+-][a-zA-z0-9]*', value)
    if res:
        flag = True
        try:
            float(value)
        except ValueError:
            flag = False
        print(flag)
    else:
        print(flag)

def digit_sum(n):
    s = 0
    while n:
        rem = n%10
        s = s+rem
        n = n//10
    print(s)

def near_pow(N,M):
    temp = (math.log(N) / math.log(M))
    low = math.pow(M, math.floor(temp))
    high = low*M

    if N-low<high-N:
        return low
    else:
        return high



if __name__ == "__main__":
    # print(check_email('golu_mishra311@.com'))
    Test_case = ['+4.50', '-1.0', '.5', '-.7','+.4', '-+.45']
    # check_float('+45')
    print(near_pow(2,4))
