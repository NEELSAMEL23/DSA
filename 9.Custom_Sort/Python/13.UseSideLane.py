def can_sort_trucks(trucks,n):
    side_lane = []
    current = 1
    
    for truck in trucks:
        while side_lane and side_lane[-1] == current:
            side_lane.pop()
            current += 1
            
        if truck == current:
            current += 1
        else:
            side_lane.append(truck)
    
    while side_lane and side_lane[-1] == current:
        side_lane.pop()
        current += 1
    
    return "yes" if current == n + 1 else "no"

n = 5
trucks = [5,1,2,4,3]
res = can_sort_trucks(trucks,n)
print(res)