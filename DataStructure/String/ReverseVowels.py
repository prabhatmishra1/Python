"""
# Write a function should reverse the vowels in a string. Any characters which are not vowels should remain in their original position. You should not consider "y" to be a vowel.
# '''
# reverse_vowels("Hello!") # "Holle!"
# reverse_vowels("Tomatoes") # "Temotaos"
# reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
# reverse_vowels("aeiou") # "uoiea"
# reverse_vowels("why try, shy fly?") # "why try, shy fly?"
"""


def reverse_vowels_in_string(s):
    arr = list(s)
    i, j = 0, len(arr)-1
    vowels = ['a', 'e', 'i', 'o', 'u']
    while i < j:
         # print(f'{arr[i]} == {arr[j]}')
         if arr[i].lower() not in vowels :
             i+=1

         if arr[j].lower() not in vowels:
            j-=1

         if arr[i] in vowels and arr[j] in vowels:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i+=1
            j-=1

    return "".join(arr)

if __name__ == "__main__":

    input = "Reverse Vowels In A String"
    # output = "RivArsI Vewols en e Streng"
    print(reverse_vowels_in_string(input))