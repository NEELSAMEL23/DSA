def count_common_elements(A, B):
    # Sorting the arrays in place
    A.sort()
    B.sort()
    
    i, j, count = 0, 0, 0
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            count += 1
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return count

arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [4, 4, 3, 2, 1, 1]
res = count_common_elements(arr1, arr2)
print(res)
