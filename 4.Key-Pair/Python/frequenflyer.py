def find_most_occured(n,arr):
    pair_map = {}
    
    for num in arr:
      if num in pair_map:
        pair_map[num] += 1
      else:
        pair_map[num] = 1
        
    max_count = -1
    result = None
    for num, count in pair_map.items():
      if count > max_count or (count == max_count and num < result):
        max_count = count
        result = num
    print(result)

N = 5
arr = [1, 1, 2, 2, 2]
find_most_occured(N,arr)
