def can_separate_digits(n, num_str):
    while len(num_str) > 1:
        found_split = False
        for i in range(1, len(num_str)):  
            left_part = num_str[:i]
            right_part = num_str[i:]
            if sum(map(int, left_part)) + sum(map(int, right_part)) > 17:
                num_str = right_part
                found_split = True
                break
        
        if not found_split:
            print("No")
            return
    
    print("Yes")

n = int(input())
num_str = input()
can_separate_digits(n, num_str)