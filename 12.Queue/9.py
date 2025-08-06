Tc = int(input().strip())
T = []
for _ in range(Tc):
    N = int(input().strip())
    h = list(map(int, input().split()))
    T.append((N, h))
r = []
for c in T:
    N, h = c
    rounds = 1  
    for i in range(1, N):
        if h[i] <= h[i - 1]:
            rounds += 1  
    r.append(rounds)
for result in r:
    print(result)