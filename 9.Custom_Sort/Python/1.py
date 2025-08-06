def merge(arr, indices, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    

    L = arr[left:mid+1]
    R = arr[mid+1:right+1]
    L_ind = indices[left:mid+1]
    R_ind = indices[mid+1:right+1]
    

    i = j = 0
    k = left
    

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            indices[k] = L_ind[i]
            i += 1
        else:
            arr[k] = R[j]
            indices[k] = R_ind[j]
            j += 1
        k += 1
    
 
    while i < n1:
        arr[k] = L[i]
        indices[k] = L_ind[i]
        i += 1
        k += 1
    
   
    while j < n2:
        arr[k] = R[j]
        indices[k] = R_ind[j]
        j += 1
        k += 1

def mergeSort(arr, indices, left, right):
    if left < right:
        mid = (left + right) // 2
        
        mergeSort(arr, indices, left, mid)
        mergeSort(arr, indices, mid + 1, right)
        merge(arr, indices, left, mid, right)



m = int(input())

arr = list(map(int, input().split()))

indices = list(range(m))

mergeSort(arr, indices, 0, m - 1)

print(' '.join(map(str, indices)))

