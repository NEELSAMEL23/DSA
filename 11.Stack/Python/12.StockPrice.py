def calculateSpan(prices, n):
    
    span = [0] * n
    stack = []
    
    span[0] = 1
    stack.append(0)
    
    for i in range(1, n):
     
        while stack and prices[i] >= prices[stack[-1]]:
            stack.pop()
        
        if stack:
            span[i] = i - stack[-1]
        else:
            span[i] = i + 1
           
        
        stack.append(i)
    
    return span

price = [100,60,70,65,80,85]  # Output - 1 1 2 1 4 5
n = 6
res = calculateSpan(price,n)
print(*res)