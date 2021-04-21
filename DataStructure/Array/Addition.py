row,col=(map(int,input("Enter the Size of matrix: ").split("*")))
print("Enter the Elements of First matirix")
mat1=[ list(map(int,input("Enter the {} row.\n".format(_)).split())) for _ in range(row)]
print("Enter the Elements of First matirix")
mat2=[ list(map(int,input("Enter the {} row.\n".format(_)).split())) for _ in range(row)]
mat3=[[0]*col]*row
print("Addition of matrix is:")
for i in range(row):
    for j in range(col):
         mat3[i][j]=mat1[i][j]+mat2[i][j]
         print(mat1[i][j]+mat2[i][j],end=" ")
    print()     


#print(mat3)     
