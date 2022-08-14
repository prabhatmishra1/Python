# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V(5) and X(10) to make 4 and 9.
# X can be placed before L(50) and C(100) to make 40 and 90.
# C can be placed before D(500) and M(1000) to make 400 and 900.


def change_roman_to_integer(arr):
    """
    this function will change roman to integer
    """
    print(arr)
    roman_data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    i = len(arr)-1
    while i >= 0:
        if (arr[i] in ['V', 'X']) and (i>0 and arr[i-1] == 'I'):
            value = roman_data[arr[i]]-roman_data[arr[i-1]]
            res = res+value
            i = i-1

        elif (arr[i] in ['L', 'C']) and (i > 0 and arr[i-1] == 'X'):
            value = roman_data[arr[i]]-roman_data[arr[i-1]]
            res = res+value
            i = i-1

        elif (arr[i] in ['D','M']) and (i > 0 and arr[i-1] == 'C'):
            value = roman_data[arr[i]]-roman_data[arr[i-1]]
            res = res+value
            i = i-1
        else:
            res = res+roman_data[arr[i]]
        i=-1
    return res
    
result = change_roman_to_integer("MMMCDXC")

print(result)

