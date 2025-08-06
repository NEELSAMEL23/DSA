MOD = 10**9 + 7

def max_path_sum(nums1, nums2):
    i = j = 0
    sum1 = sum2 = 0
    result = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            sum1 += nums1[i]
            i += 1
        elif nums1[i] > nums2[j]:
            sum2 += nums2[j]
            j += 1
        else:
            result += max(sum1, sum2) + nums1[i]
            sum1 = sum2 = 0
            i += 1
            j += 1

    result += max(sum1 + sum(nums1[i:]), sum2 + sum(nums2[j:]))
    return result % MOD

# Main function to handle multiple test cases
T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    print(max_path_sum(nums1, nums2))
