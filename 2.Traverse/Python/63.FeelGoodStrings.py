n = int(input())
s = input()

vowels = set('aeiou')
vowel_count = sum(1 for ch in s if ch in vowels)

if vowel_count >= n // 2:
    print("Feel good!")
else:
    print("Feel bad!")
