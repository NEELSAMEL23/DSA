from collections import deque

def follow_the_knight(i, j, N):
    directions = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
   
    queue = deque()
    queue.append((i, j, 0))
    
    visited = set()
    result = set()
    
    while queue:
        x, y, moves = queue.popleft()
        
        if moves == N:
            result.add((x, y))
            continue
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 1 <= nx <= 10 and 1 <= ny <= 10:
                queue.append((nx, ny, moves + 1))
    
    print(len(result))


i, j, N = map(int, input().split())
follow_the_knight(i, j, N)
