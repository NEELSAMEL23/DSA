def two_sum(N,B,arr):
    left, right = 0, N - 1
    found = False
            
    while left < right:
      current_sum = arr[left] + arr[right]
                
      if current_sum == B:
        print(left, right)
        found = True
        break
      elif current_sum < B:
        left += 1
      else:
        right -= 1
            
    if not found:
      return "-1 -1"
      
N = 4
B = 9
arr = [2,7,11,15]
res = two_sum(N,B,arr)
print(res)