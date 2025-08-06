n = int(input())
s = input()

freq = {}


for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for char in sorted(freq):
    print(f"{char}-{freq[char]}")
