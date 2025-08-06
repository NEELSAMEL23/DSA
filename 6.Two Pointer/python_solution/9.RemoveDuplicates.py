def remove_Duplicated(arr,N):
  j = 0
  
  for i in range(1,N):
    if arr[i] != arr[j]:
      j+=1
      arr[j] = arr[i]
      
  return j + 1, arr[:j + 1]

arr = [1,1,2,2]
N = 4
unique_count,unique_elements = remove_Duplicated(arr,N)

print(unique_count)
print(*unique_elements)