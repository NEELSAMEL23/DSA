def super_digit(n):
    if len(n) == 1:
        return int(n)

    total = sum(int(digit) for digit in n)
    return super_digit(str(total))


t = int(input())
for _ in range(t):
  n = input().strip()
  print(super_digit(n))