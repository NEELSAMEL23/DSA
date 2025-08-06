def process_queries(queries):
    queue = []
    stack = []
    result = []
    
    for query in queries:
        if query[0] == 1:  
            queue.append(query[1])
        
        elif query[0] == 2:  
            stack.append(query[1])
        
        elif query[0] == 3:  
            if queue:
                result.append(queue[0])
            else:
                result.append(-1)
        
        elif query[0] == 4: 
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)
        
        elif query[0] == 5:  
            if queue:
                stack.append(queue.pop(0))
            else:
                result.append(-1)
    
    return result

Q = 7
queries = ["1 4","2 3","1 2","3","4","5","4"]

outputs = process_queries(queries)
