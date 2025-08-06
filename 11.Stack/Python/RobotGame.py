n = int(input())
swords = list(map(int, input().split()))
directions = input().strip()

stack = []  # Will hold tuples of (sword_length, direction)

for i in range(n):
    curr_sword = swords[i]
    curr_dir = directions[i]

    if curr_dir == '1':
        stack.append((curr_sword, curr_dir))
    else:  # curr_dir == '0'
        while stack and stack[-1][1] == '1':
            top_sword, _ = stack[-1]
            if top_sword < curr_sword:
                stack.pop()
            elif top_sword == curr_sword:
                stack.pop()
                curr_sword = -1  # both die
                break
            else:
                curr_sword = -1  # current robot dies
                break
        if curr_sword != -1:
            stack.append((curr_sword, curr_dir))

# Print remaining sword lengths
print(*[sword for sword, _ in stack])
