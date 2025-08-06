def recursion_sum(arr,n):
    if n == 0:
        return 0
    else:
        return arr[n-1] + recursion_sum(arr,n-1)

arr = [1,2,3,4]
n = 4
res = recursion_sum(arr,n)
print(res)