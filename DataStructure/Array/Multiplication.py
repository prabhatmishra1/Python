row1,col1=(map(int,input("Enter the Size of  first matrix: ").split("*")))
print("Enter the Elements of First matirix")
mat1=[ list(map(int,input("Enter the {} row.\n".format(_)).split())) for _ in range(row1)]
row2,col2=(map(int,input("Enter the Size of  second matrix: ").split("*")))
print("Enter the Elements of First matirix")
mat2=[ list(map(int,input("Enter the {} row.\n".format(_)).split())) for _ in range(row2)]
#mat3=[[0]*col2]*row1
print("Multiplication of matrix is:")

for i in range(row1):
    for j in range(col2):
         #print(mat1[i][j]*mat2[0][j]+mat1[i][j]*mat2[1][j],end=" ")
        s=0
        for k in range(col1):
            s=s+mat1[i][k]*mat2[k][j]
        print(s,end=" ")
            
    print()     

    
