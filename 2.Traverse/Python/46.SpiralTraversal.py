def counterclockwise_spiral_traversal(matrix, N, M):
    top, bottom = 0, N - 1
    left, right = 0, M - 1
    
    while top <= bottom and left <= right:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=" ")
        left += 1

        if left <= right:
            for i in range(left, right + 1):
                print(matrix[top][i], end=" ")
            top += 1
        
       
        if top <= bottom:
            for i in range(top, bottom + 1):
                print(matrix[i][right], end=" ")
            right -= 1
        
        if left <= right:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1
        
    print()  
    
matrix = [ 
          [1,2,3,4], 
          [5,6,7,8] , 
          [9,10,11,12]
          ] 
N = 3
M = 4
counterclockwise_spiral_traversal(matrix, N, M)

# Output:-9 5 1 2 3 4 8 12 11 10 6 7 