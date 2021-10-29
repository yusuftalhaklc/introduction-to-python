#matrix addition
matrix1 = [[1,3,5],[2,4,1],[1,5,7]]
matrix2 = [[3,3,4],[2,4,1],[3,5,4]]
sumofmatrices = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1)):
        sumofmatrices[i][j] = matrix1[i][j] + matrix2[i][j]
print(sumofmatrices)

#What do we want to do ?
"""
1 3 5     3 3 4    4 6 9
2 4 1  +  2 4 1 =  4 8 2
1 5 7     3 5 4    4 10 11
"""
#output
# [4, 6, 9], [4, 8, 2], [4, 10, 11]]