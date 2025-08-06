def Traverse_arr(arr,N,M):
    for col in range(M):
        even_sum = 0
        for row in range(N):
            if arr[row][col] % 2 ==0:
                even_sum += arr[row][col]
        print(even_sum)
    
arr = [ 
       [1,2,3],
       [4,5,6],
       [7,8,9], 
    ] 
N = 3
M = 3
Traverse_arr(arr,N,M)

# Output:-
# 4
# 10
# 6