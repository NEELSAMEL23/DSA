def time_to_minutes(t):
    h, m = map(int, t.split(':'))
    return h * 60 + m

def min_platforms_required(n, arr, dep):
    # Convert time strings to minutes
    arr = [time_to_minutes(t) for t in arr]
    dep = [time_to_minutes(t) for t in dep]
    
    arr.sort()
    dep.sort()
    
    i = 1  
    j = 0 
    platforms = 1 
    max_platforms = 1 

    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms += 1
            i += 1
        else:
            platforms -= 1
            j += 1
        max_platforms = max(max_platforms, platforms)

    return max_platforms


n = 6
arr = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
dep = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

res = min_platforms_required(n, arr, dep)
print(res)
