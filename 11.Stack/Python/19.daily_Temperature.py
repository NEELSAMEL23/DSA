def solve(n,arr):
  
  result = []
  answers = [0] * n
  stack = []
  
  for day in range(n-1,-1,-1):
    while stack and arr[day] >= arr[stack[-1]]:
      stack.pop()
      
    if stack:
      answers[day] = stack[-1] - day
    else:
      answers[day] = 0
    
    stack.append(day)
    
  print(*answers)


arr = [73, 74, 75, 71, 69, 72, 76, 73]
n = 8
solve(n,arr)
  