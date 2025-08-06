def pairMatch(pairs):

    pair_map = {")":"(","}":"{","]":"["}      
    stack = []

    for char in pairs:

        if char in pair_map.values():
            stack.append(char)
        elif char in pair_map:
            if stack and pair_map[char] != stack[-1]:
                return False
    return True           
pairs = "{[()]}"
res = pairMatch(pairs)
print(res)
