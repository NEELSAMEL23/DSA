def sum_boundary_daigonal(arr,N):
    sum = 0

    for j in range(N):
        sum += arr[0][j]
        
    for j in range(N):
        sum +=arr[N-1][j]
        
    for i in range(1,N-1):
        sum +=arr[i][0]
        
    for i in range(1,N-1):
        sum +=arr[i][N-1]
        
    for i in range(1,N-1):
        sum +=arr[i][i]
        
    for i in range(1,N-1):
        if i !=N-i-1:
            sum +=arr[i][N-i-1]
            
    return sum

arr = [
    [1,2,3,4,5],
    [6,7,8,9,1],
    [2,3,4,5,6],
    [7,8,9,1,2],
    [3,4,5,6,7]
]
N = 5

res = sum_boundary_daigonal(arr,N)
print(res)