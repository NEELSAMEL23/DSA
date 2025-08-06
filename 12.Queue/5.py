def find_starting_point(n, stations):
   
    total_energy = sum([station[0] for station in stations])
    total_distance = sum([station[1] for station in stations])

   
    if total_energy < total_distance:
        return "No starting points"

    
    current_energy = 0
    start_index = 0

    for i in range(n):
        energy, distance = stations[i]
        current_energy += energy - distance

        
        if current_energy < 0:
            start_index = i + 1
            current_energy = 0

    return start_index if start_index < n else "No starting points"


n = int(input()) 
stations = [tuple(map(int, input().split())) for _ in range(n)]


print(find_starting_point(n, stations))
