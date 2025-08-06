def count_cool_subarrays(n, k, arr):
    if k > n:
        return 0

    count = 0
    freq = {}
    
    for i in range(k):
        freq[arr[i]] = freq.get(arr[i], 0) + 1
    
    if len(freq) == k:
        count += 1

    for i in range(k, n):
        # Remove the leftmost element
        freq[arr[i-k]] -= 1
        if freq[arr[i-k]] == 0:
            del freq[arr[i-k]]

        # Add the current element
        freq[arr[i]] = freq.get(arr[i], 0) + 1

        if len(freq) == k:
            count += 1

    return count

# Main Execution
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(count_cool_subarrays(n, k, arr))
