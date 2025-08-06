

def square_matrix(matrix,N,M):

    for row in range(N):
        for col in range(M):
            matrix[row][col] += 1
    for i in matrix:
        print(" ".join(map(str,i)))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
N = 3
M = 4
square_matrix(matrix,N,M)
