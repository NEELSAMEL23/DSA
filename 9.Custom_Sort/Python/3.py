def sort_out_indices(arr):
    indexed_arr = [(arr[i], i) for i in range(len(arr))]
    
  
    for i in range(len(indexed_arr)):
        for j in range(0, len(indexed_arr) - i - 1):
            if indexed_arr[j][0] > indexed_arr[j + 1][0]:
                indexed_arr[j], indexed_arr[j + 1] = indexed_arr[j + 1], indexed_arr[j]
    
   
    sorted_indices = [index for value, index in indexed_arr]
    return sorted_indices


m = int(input())  
arr = list(map(int, input().split()))  

result = sort_out_indices(arr)
print(*result)
