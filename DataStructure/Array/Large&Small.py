arr=list(int(input("Enter the value at index {}: ".format(_))) for _ in range(int(input("Enter the Size of Array: "))))

small=arr[0]
large=arr[0]

for i in arr:
    if i>large:
        large=i

    if i<small:
        small=i


print("Largest value of array is {}".format(large))
print("Smallest value of array is {}".format(small))



print(max(arr))
print(min(arr))
