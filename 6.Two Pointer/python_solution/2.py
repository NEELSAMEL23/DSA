def find_pair_count(arr, k):
  arr.sort()
  i = 0
  j = len(arr) - 1
  count = 0
    
  while i < j:
    if arr[i] + arr[j] == k:
      count += 1
      i += 1
      j -= 1
    elif arr[i] + arr[j] < k:
      i += 1
    else:
      j -= 1
            
  return count


arr = [3, 0, 2, 6, 7]
k = 9
res = find_pair_count(arr, k)
print(res)
