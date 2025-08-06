# Traverse 2d array
def Traverse_arr(arr,N,M):
    matrix = []
    for col in range(M):
        for row in range(N-1,-1,-1):
            matrix.append(arr[row][col])

    return " ".join(map(str,matrix))

arr = [ 
       [1,8,9], 
       [2,7,10],
       [3,6,11], 
       [4,5,12]
    ] 
N = 4
M = 3
res = Traverse_arr(arr,N,M)
print(res)
# Output:- 4 3 2 1 5 6 7 8 12 11 10 9