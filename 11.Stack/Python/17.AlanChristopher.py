s = "abc#d##c"
result = []

for ch in s:
    if ch == '#':
        if result:
            result.pop()
    else:
        result.append(ch)

print("".join(result))
