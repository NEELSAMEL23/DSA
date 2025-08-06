def count_non_repetitive_substrings(S, K):
    count = 0
    for i in range(len(S) - K + 1):
        substring = S[i:i+K]
        if len(set(substring)) == K:
            count += 1
    return count

T = int(input())
for _ in range(T):
    S = input().strip()
    K = int(input())
    result = count_non_repetitive_substrings(S, K)
    print(result)
