row= int(input("Enter the number of rows: "))

col= int(input("Enter the number of cloumns: "))

mat3=[[0 for j in range(col)] for i in range(row)]

print("Enter elemenets of the First matrix:")

mat1=[[eval(input()) for j in range(col)] for i in range(row)]
print("First matrix is: ")
for i in range(row):
    for j in range(col):
        print("{:5d}".format(mat1[i][j]),end=" ")
    print()
print(mat1)

print("Enter elemenets of the second matrix:")

mat2=[[int(input()) for j in range(col)] for i in range(row)]
print("Second matrix is: ")

for i in range(row):
    for j in range(col):
        print("{:5d}".format(mat2[i][j]),end=" ")
    print()

print("_____________________________________________________________________________________________________________________________________________________\n")

#addition of matrix is
for i in range(row):
    for j in range(col):
        mat3[i][j]=mat1[i][j]+mat2[i][j]


print("Addition of matrix is:")

for i in range(row):
    for j in range(col):
        print("{:5d}".format(mat3[i][j]),end=" ")
    print()


#subtraction matrix
for i in range(row):
    for j in range(col):
        mat3[i][j]=mat1[i][j]-mat2[i][j]


print("Subtraction of matrix is:")

for i in range(row):
    for j in range(col):
        print("{:5d}".format(mat3[i][j]),end=" ")
    print()


#transposition of matrix:
print("Transposition of matrix is:")    
for i in range(row):
    for j in range(col):
        print("{:5d}".format(mat1[j][i]),end=" ")
    print()
    

s=0
#multiplication of matrix:
print("multiplication of matrix is:")    
for i in range(row):
    for j in range(col):
        s=0
        for k in range(row):
            s=s+mat1[i][k]*mat2[k][j]
        mat3[i][j]=s

for i in range(row):
    for j in range(col):
        print("{:5d}".format(mat3[i][j]),end=" ")
    print()



