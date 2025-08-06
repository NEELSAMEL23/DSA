def gasStation(N, gas, cost):
    total_gas = 0
    total_cost = 0
    tank = 0
    start_index = 0

    for i in range(N):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]

        if tank < 0:
            start_index = i + 1
            tank = 0

    if total_gas < total_cost:
        print(-1)
    else:
        print(start_index)


N = int(input())
gas = list(map(int, input().split()))
cost = list(map(int, input().split()))
gasStation(N, gas, cost)
