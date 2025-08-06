from collections import deque

def implement_stack_using_queue(queries):
    q1 = deque()
    q2 = deque()
    result = []
    
    for query in queries:
        if query[0] == 0:
            # Push operation
            val = query[1]
            q2.append(val)
            while q1:
                q2.append(q1.popleft())
            q1, q2 = q2, q1
        
        elif query[0] == 1:
            # Top operation - just peek front of q1
            if q1:
                result.append(q1[0])
        
        elif query[0] == 2:
            # Pop operation - print and remove front of q1
            if q1:
                result.append(q1.popleft())
    
    return result

# Input reading
q = int(input())
queries = []
for _ in range(q):
    parts = list(map(int, input().split()))
    queries.append(parts)

# Process
output = implement_stack_using_queue(queries)
for val in output:
    print(val)
