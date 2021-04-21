row,col=(map(int, input("Enter the size of Matrix: ").split("*")))

#mat=[[0]*n]*m

'''for i in range(m):
    for j in range(n):
        mat[i][j]=int(input("Enter the element at index [{} {}]: ".format(i,j)))
 '''
mat=[list(map(int,input().split())) for i in range(row)]

print(mat)
