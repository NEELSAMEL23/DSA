# Traverse 2d array
def Traverse_arr(arr,N,M):
    matrix = []
    for col in range(M-1,-1,-1):
        for row in range(N):
            matrix.append(arr[row][col])

    return " ".join(map(str,matrix))



arr = [ [1,8,9], [2,7,10] , [3,6,11], [4,5,12]] 

N = 4
M = 3
res = Traverse_arr(arr,N,M)
print(res)

# Output:-9 10 11 12 8 7 6 5 1 2 3 4