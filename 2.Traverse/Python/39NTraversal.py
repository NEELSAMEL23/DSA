def Traverse_arr(arr,N,M):
    matrix =[]

    for i in range(N-1,-1,-1):
        matrix.append(arr[i][0])

    for i in range(1,N):
        matrix.append(arr[i][i])

    
    for i in range(N-2,-1,-1):
        matrix.append(arr[i][M-1])

    return " ".join(map(str,matrix))
    
arr = [ 
       [1,2,3],
       [4,5,6],
       [7,8,9], 
    ] 
N = 3
M = 3
res = Traverse_arr(arr,N,M)
print(res)
# Output:- 4 3 2 1 5 6 7 8 12 11 10 9