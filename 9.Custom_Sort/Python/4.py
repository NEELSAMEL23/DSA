def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def sort_by_digit_sum(arr):
    return sorted(arr, key=lambda x: (digit_sum(x), x))


t = int(input())  

for _ in range(t):
    n = int(input()) 
    arr = list(map(int, input().split()))  
    sorted_arr = sort_by_digit_sum(arr)
    print(*sorted_arr) 
