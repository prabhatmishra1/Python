a1 = [1, 5, 8, 12, 15, 20, 25]
a2 = [2, 3, 6, 9, 11, 13, 16, 18, 22, 23, 30, 50]
a3 = []
n = max(len(a1),len(a2))
j = 0
i= 0
while i < n:
    if a1[j] < a2[i] and j < len(a1):
        a3.append(a1[j])
        j += 1
    else:
        a3.append(a2[i])
        i += 1
print(a3)
