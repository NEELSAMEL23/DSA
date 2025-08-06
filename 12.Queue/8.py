def can_ankush_win(s):
    queue = []
    moves = 0

    for char in s:
        if queue and ((queue[-1] == '0' and char == '1') or (queue[-1] == '1' and char == '0')):
            queue.pop()  
            moves += 1   
        else:
            queue.append(char)  

    
    return "YES" if moves % 2 == 1 else "NO"


t = int(input())
for _ in range(t):
    s = input().strip()
    print(can_ankush_win(s))