def arrange_medals(n, participants):
    # Initialize counts for 0 (Gold), 1 (Silver), and 2 (Bronze)
    count_gold = 0
    count_silver = 0
    count_bronze = 0
    
    # Count occurrences of each medal type
    for medal in participants:
        if medal == 0:
            count_gold += 1
        elif medal == 1:
            count_silver += 1
        else:
            count_bronze += 1
    
    # Output the sorted order (all Golds, then Silvers, then Bronzes)
    result = [0] * count_gold + [1] * count_silver + [2] * count_bronze
    return result

participants = [2,0,1]
n = 3
res = arrange_medals(n, participants)
print(*res)

