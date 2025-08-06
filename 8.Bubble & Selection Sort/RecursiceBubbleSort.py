def bubble_sort_recursive(arr, n):
    # Base case
    if n == 1:
        return

    # One pass of bubble sort
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call for remaining array
    bubble_sort_recursive(arr, n - 1)


n = int(input())
arr = list(map(int, input().split()))
bubble_sort_recursive(arr, n)
print(*arr)
