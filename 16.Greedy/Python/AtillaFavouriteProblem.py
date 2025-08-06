def atillas_favorite_problem(t, testcases):
    results = []

    for n, s in testcases:
        max_char = max(s)
        alphabet_size = ord(max_char) - ord('a') + 1
        results.append(alphabet_size)

    return results

# ✅ Sample Input
t = 5
testcases = [
    (1, "a"),
    (4, "down"),
    (11, "masaischool"),
    (3, "bcf"),
    (5, "zzzzz")
]

# ✅ Output
output = atillas_favorite_problem(t, testcases)
for val in output:
    print(val)
