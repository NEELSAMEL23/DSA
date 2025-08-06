from collections import Counter

k = int(input())
for _ in range(k):
    s = input().strip()
    t = input().strip()
    
    count_s = Counter(s)
    count_t = Counter(t)
    
    steps = 0
    all_chars = set(count_s.keys()).union(set(count_t.keys()))
    
    for char in all_chars:
        steps += abs(count_s.get(char, 0) - count_t.get(char, 0))
    
    print(steps)
