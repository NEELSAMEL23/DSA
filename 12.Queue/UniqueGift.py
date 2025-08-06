from collections import deque, defaultdict

def unique_gift(t, test_cases):
    results = []
    for s in test_cases:
        freq = defaultdict(int)
        queue = deque()
        res = []
        
        for ch in s:
            freq[ch] += 1
            queue.append(ch)
            
            # Remove non-unique chars from the front
            while queue and freq[queue[0]] > 1:
                queue.popleft()
            
            if queue:
                res.append(queue[0])
            else:
                res.append('#')
        
        results.append(''.join(res))
    
    return results


# Reading input
t = int(input())
test_cases = [input().strip() for _ in range(t)]

# Processing
answers = unique_gift(t, test_cases)

# Output
for ans in answers:
    print(ans)
