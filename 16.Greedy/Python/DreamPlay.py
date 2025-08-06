def lexicographically_smallest_string(n, a):
    b = []
    res = []
    
    for i in range(n):
        b.append(a[i])
        
        # Find the smallest character in the remaining A[i+1:]
        smallest = min(a[i+1:]) if i + 1 < n else None

        # Pop from B while top is <= smallest character remaining in A
        while b and (smallest is None or b[-1] <= smallest):
            res.append(b.pop())

    # Pop remaining characters from B
    while b:
        res.append(b.pop())

    print(''.join(res))

# Input
n = int(input())
a = input().strip()
lexicographically_smallest_string(n, a)
