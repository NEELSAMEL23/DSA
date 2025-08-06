def generate_combinations(digits, index, current_combination, result, phone_map):
    if index == len(digits):
        result.append(current_combination)
        return

    digit = digits[index]
    letters = phone_map.get(digit, [])

    if not letters:
        return

    for letter in letters:
        generate_combinations(digits, index + 1, current_combination + letter, result, phone_map)

# Define phone keypad mapping
phone_map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

# Hardcoded input
digits = "23"

# Generate combinations
result = []
generate_combinations(digits, 0, '', result, phone_map)

# Print output
print(' '.join(result))
