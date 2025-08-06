# Corner column sum

def Traverse_arr(arr,N,M):

    sum = 0

    for i in range(N):
        sum += arr[i][0]
        sum += arr[i][M-1]
    return sum


arr = [ 
       [1,2,7],
       [3,4,6],
       [5,6,10], 
    ] 
N = 3
M = 3
res = Traverse_arr(arr,N,M)
print(res)
