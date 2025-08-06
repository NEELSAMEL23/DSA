def nearestGreaterElement(arr, n):
    result = [-1] * n
    stack = []

  
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)
    
    return result


n = 8
arr = [39,27,11,4,24,32,32,1]

res = nearestGreaterElement(arr, n)
print(res)