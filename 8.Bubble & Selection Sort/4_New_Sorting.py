
arr = [12, 18, 17, 65, 46]
k = 6

sorted_arr = sorted(arr, key=lambda x: x % k)

print(*sorted_arr)
