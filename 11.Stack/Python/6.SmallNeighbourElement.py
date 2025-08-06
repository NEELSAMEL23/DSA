def nearest_smaller_elements(arr,n):
    stack = []
    result = []
  
    for i in range(len(arr)):
        while stack and stack[-1] >= arr[i]:
          stack.pop()
      
        if stack:
          result.append(stack[-1])
        else:
          result.append(-1)
      
        stack.append(arr[i])
  
    return result
  
n = 8
arr = [39,27,11,4,24,32,32,1]

res = nearest_smaller_elements(arr,n)
print(res)