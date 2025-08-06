def spiral_matrix(n, arr):
    matrix = [[0] * n for _ in range(n)]
    

    top, bottom = 0, n - 1
    left, right = 0, n - 1
    
    index = 0  
    
    while index < len(arr):
        for i in range(left, right + 1):
            if index < len(arr):
                matrix[top][i] = arr[index]
                index += 1
        top += 1
        
        for i in range(top, bottom + 1):
            if index < len(arr):
                matrix[i][right] = arr[index]
                index += 1
        right -= 1
        
        for i in range(right, left - 1, -1):
            if index < len(arr):
                matrix[bottom][i] = arr[index]
                index += 1
        bottom -= 1
        
        for i in range(bottom, top - 1, -1):
            if index < len(arr):
                matrix[i][left] = arr[index]
                index += 1
        left += 1
    
    return matrix

def sum_of_diagonals(matrix, n):
    diagonal_sum = 0
    
    for i in range(n):
        diagonal_sum += matrix[i][i]
       
        if i != n - i - 1:
            diagonal_sum += matrix[i][n - i - 1]
    
    return diagonal_sum

  

arr = [1 ,2,3, 4, 8, 12, 16, 15, 14, 13, 9 ,5 ,6 ,7 ,11, 10]
 

matrix = spiral_matrix(N, arr)
res = sum_of_diagonals(matrix, N)

print(res)


