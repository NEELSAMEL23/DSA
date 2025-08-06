t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    
    called = set()
    
    for i in range(n):
        current_id = i + 1
        if current_id not in called:
            called.add(A[i])
    
    never_called = [i for i in range(1, n+1) if i not in called]
    print(len(never_called))
    print(*sorted(never_called))
