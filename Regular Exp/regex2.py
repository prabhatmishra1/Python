'''Write a Python Program to check whether the given number
is valid mobile number or not?
'''
import re
f1 = open("D:\python\Regular Exp\phone.txt", "r")
file_data = f1.read()

s = re.findall('[6-9][0-9]{9}', file_data)
f1.close()
print(*s)
f2 = open("D:\python\Regular Exp\phone_output.txt", "w")
f2.write('\n'.join(s))
f2.close()