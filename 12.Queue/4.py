def first_unique_gift(stream):
    queue = []
    frequency = {}
    result = []
    
    for char in stream:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
            queue.append(char)
        
       
        while queue and frequency[queue[0]] > 1:
            queue.pop(0)
        
        if queue:
            result.append(queue[0])
        else:
            result.append('#')
    
    return ''.join(result)

stream = "abadbc"
res = first_unique_gift(stream)
print(res)
