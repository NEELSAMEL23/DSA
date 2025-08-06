def square_sort(arr):
    return sorted(arr, key=lambda x: x * x)


arr = [-2, 3, 1, -4, 6]
res = square_sort(arr)
print(" ".join(map(str,res)))
