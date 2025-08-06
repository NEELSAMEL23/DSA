def max_items_within_budget(prices, budget):
    start = 0
    total = 0
    max_count = 0

    for end in range(len(prices)):
        total += prices[end]
        
        while total > budget:
            total -= prices[start]
            start += 1
        
        max_count = max(max_count, end - start + 1)

    return max_count

# Input
prices = list(map(int, input().split()))
budget = int(input())

# Output
print(max_items_within_budget(prices, budget))
