def spiral_traverse(matrix, N, M):
    top = 0 
    bottom = N - 1 
    left = 0 
    right = M - 1
  
    arr = []
  
    while top <= bottom and left <= right:
 
        for i in range(top, bottom + 1):
            arr.append(matrix[i][left])
        left += 1
    
  
        for j in range(left, right + 1):
            arr.append(matrix[bottom][j])
        bottom -= 1 
    
        if left <= right:
       
            for i in range(bottom, top - 1, -1):
                arr.append(matrix[i][right])
            right -= 1
    
        if top <= bottom:
            
            for j in range(right, left - 1, -1):
                arr.append(matrix[top][j])
            top += 1
    
    return " ".join(map(str, arr))

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
N = 3
M = 4
res = spiral_traverse(matrix,N,M)
print(res)