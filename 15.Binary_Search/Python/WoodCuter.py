def wood_collected(trees, saw_height):
    return sum(tree - saw_height for tree in trees if tree > saw_height)

def find_max_height(trees, required_wood):
    low = 0
    high = max(trees)
    result = 0

    while low <= high:
        mid = (low + high) // 2
        collected = wood_collected(trees, mid)

        if collected >= required_wood:
            result = mid  # try to go higher
            low = mid + 1
        else:
            high = mid - 1

    return result

# Input handling
n, m = map(int, input().split())
trees = list(map(int, input().split()))

print(find_max_height(trees, m))
