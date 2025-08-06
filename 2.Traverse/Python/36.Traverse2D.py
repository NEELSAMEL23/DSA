# Go in Zig zag
def Traverse_arr(matrix,N,M):
    arr = []
    
    for row in range(N):
        if row % 2 ==0:
            for col in range(M-1,-1,-1):
                arr.append(matrix[row][col])
        else:
            for col in range(M):
                arr.append(matrix[row][col])
    
    return "".join(map(str,arr))

matrix = [ 
       [1,2,3,4,5],
       [6,7,8,9,1],
       [3,2,5,4,6], 
       [7,8,9,1,2]
    ] 
N = 4
M = 5
res = Traverse_arr(matrix,N,M)
print(res)
# Output:- 12 11 10 9 5 6 7 8 4 3 2 1