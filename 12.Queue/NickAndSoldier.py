from collections import deque

def nick_and_soldiers(n, m, powers):
    queue = deque([(i + 1, powers[i]) for i in range(n)])  # (original_position, power)
    result = []

    for _ in range(m):
        temp = []

        # Step 1: Pull up to M soldiers from queue
        count = min(m, len(queue))
        for _ in range(count):
            temp.append(queue.popleft())

        # Step 2: Find the max power soldier (first in case of tie)
        selected = max(temp, key=lambda x: x[1])
        result.append(selected[0])  # original position

        # Step 3: Re-enqueue others (decrementing power)
        for soldier in temp:
            if soldier != selected:
                updated_power = max(0, soldier[1] - 1)
                queue.append((soldier[0], updated_power))

    print(" ".join(map(str, result)))

# Read input from STDIN (if using in a platform like Masai/LeetCode)
n, m = map(int, input().split())
powers = list(map(int, input().split()))
nick_and_soldiers(n, m, powers)
