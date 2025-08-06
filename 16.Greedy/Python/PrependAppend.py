def find_original_length(s):
    first_1 = s.find('1')
    last_0 = s.rfind('0')
    if first_1 == -1 or last_0 == -1 or last_0 < first_1:
        return 0
    return last_0 - first_1 + 1

T = int(input())
for _ in range(T):
    n = int(input())
    s = input().strip()
    print(find_original_length(s))
