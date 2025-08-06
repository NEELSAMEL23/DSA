def z_traversal(matrix, N):
    for i in range(N):
        print(matrix[0][i], end=" ")


    for i in range(1, N-1):
        print(matrix[i][N-i-1], end=" ")

    for i in range(N):
        print(matrix[N-1][i], end=" ")
    print() 
    
matrix = [ 
          [1,2,3], 
          [4,5,6] , 
          [7,8,9]
          ] 
N = 3
z_traversal(matrix, N)