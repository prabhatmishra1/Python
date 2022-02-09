''' App1: Write a Regular Expression to represent all Yava language identifiers'''

'''
Rules:
1. The allowed characters are a-z,A-Z,0-9,#
2. The first character should be a lower case alphabet symbol from a to k
3. The second character should be a digit divisible by 3
4. The length of identifier should be atleast 2
'''
import re

def check_yava(value):
    s = re.fullmatch('[a-k][0369][a-zA-z0-9#]*',value)
    if s:
      print("right")
    else:
        print("wrong")


def check_mobile(mobile):
    s = re.fullmatch('[6-9][0-9]{9}', mobile)
    if s:
      print("right")
    else:
        print("wrong")


if __name__ == "__main__":
    # check_yava('a')
    check_mobile('8140238580')




