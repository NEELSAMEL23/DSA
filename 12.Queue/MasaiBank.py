from collections import deque

Q = int(input())
queue = deque()

for _ in range(Q):
    inp = input().strip()
    
    if inp.startswith("1"):
        _, val = inp.split()
        queue.append(val)
        
    elif inp == "2":
        if queue:
            print(queue.popleft())
        else:
            print("No More Tokens")
