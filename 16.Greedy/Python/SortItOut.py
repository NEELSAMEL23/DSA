def minOperationsToSort(n,permutation):
  max_len = 1
  curr_len = 1
  
  for i in range(1,n):
    if permutation[i] > permutation[i - 1]:
      curr_len += 1
    else:
      max_len = max(max_len,curr_len)
      
  max_len = max(max_len,curr_len)
  
  res = n - max_len
  print(res)