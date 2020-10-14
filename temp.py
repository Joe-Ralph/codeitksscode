def search(mat,key):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==key:
                return (i,j)
    return (-1,-1)

mat =[[1,2,3],[4,5,6],[7,8,9]]
search(mat,9)