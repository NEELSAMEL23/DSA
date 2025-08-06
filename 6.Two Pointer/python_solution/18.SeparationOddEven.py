def separation_of_odd_even(N, arr, Q):
    left = 0
    right = N - 1
    
    # Use two-pointer technique to rearrange the array
    while left < right:
        if arr[left] % 2 == 0:
            left += 1
        elif arr[right] % 2 != 0:
            right -= 1
        else:
            # Swap if left is odd and right is even
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    # Return based on the value of Q
    if Q == 1:
        return " ".join(map(str, arr))
    elif Q == 2:
        # Invert the order to have odd numbers first
        return " ".join(map(str, arr[::-1]))

# Test cases
arr1 = [1, 2, 3, 4, 5] 
Q = 1
N = 5
res = separation_of_odd_even(N, arr1, Q)
print(res)

arr2 = [1, 2, 3, 4, 5] 
Q = 2
N = 5
res = separation_of_odd_even(N, arr2, Q)
print(res)
