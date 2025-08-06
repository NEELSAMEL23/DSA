def solve(N, A):
    total_sum = sum(A)
    left_sum = 0
    
    for i in range(1, N - 1):
        left_sum += A[i - 1]
        right_sum = total_sum - left_sum - A[i]
        
        if left_sum == right_sum:
            print(i)
            return
    
    print(-1)


n=5
arr = [15 ,1 ,5 ,5 ,5]
solve(n, arr)
