def solve(N,arr):
    output = [1] * N
    left_product = 1

    for i in range(N):
        output[i] = left_product
        left_product *= arr[i]

    right_product = 1
    for i in range(N - 1, -1, -1):
        output[i] *= right_product
        right_product *= arr[i]

    return output

N = 4
arr = [1, 2, 3, 4]
res = solve(N,arr)
print(res)