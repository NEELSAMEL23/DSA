def pair_less_than_k(arr,k):
    arr.sort()
    i = 0
    j = len(arr)-1
    max_pair = -1
   
    while i < j:
        current = arr[i]+arr[j]

        if current < k:
            max_pair = max(max_pair,current)
            i += 1
        else:
            j-=1
    return max_pair


arr1 = [1 ,2, 3, 4, 5]
arr2 = [15 ,2, 30]
k = 7
res = pair_less_than_k(arr1,k)
print(res)
