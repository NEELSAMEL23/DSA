def can_pour_into_two_buckets(a, b):
    total_water = sum(a)  # Total water in all buckets
    # Find the two largest bucket capacities
    max1 = max(b)  # First largest capacity
    b.remove(max1)
    max2 = max(b)  # Second largest capacity
    
    # Check if the total water can fit into two largest buckets
    if total_water <= max1 + max2:
        return "YES"
    else:
        return "NO"

a = [3,5]
b = [3,6]
res = can_pour_into_two_buckets(a, b)
print(res)