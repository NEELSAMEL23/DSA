def generate_binaries(n, curr, result):
    if len(curr) == n:
        result.append(curr)
        return

    # Always can add '1'
    generate_binaries(n, curr + '1', result)

    # Add '0' only if previous char is not '0'
    if not curr or curr[-1] != '0':
        generate_binaries(n, curr + '0', result)

def solve():
    t = int(input())
    for _ in range(t):
        k, n = map(int, input().split())  # k is unused here
        result = []
        generate_binaries(n, "", result)
        result.sort()
        print(" ".join(result))

# Example usage:
# Input:
# 2
# 1 1
# 1 3
# Output:
# 0 1
# 010 011 101 110 111

solve()
