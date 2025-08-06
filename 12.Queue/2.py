def process_queries(K, queries):
    queue = []
    result = []
    
    for querie in queries:
        querie = querie.split()

        if querie[0] == "1":
            if len(queue) < K:
                queue.append(querie[1])
                result.append(querie[1])
            else:
                result.append("-1")
        elif querie[0] == "2":
            if queue == []:
                result.append("-1")
            else:
                result.append(str(queue.pop(0)))
    return "\n".join(result)

# Directly assigned values for testing
K = 2
Q = 6
queries = ["1 1","1 2","1 3","2","2","2"]

# Process queries
res = process_queries(K, queries)
print(res)
