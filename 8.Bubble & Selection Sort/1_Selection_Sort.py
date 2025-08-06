def selection_sort(arr,n):

    for i in range(n-1):
        min_indx = i
        for j in range(i+1,n):

            if arr[j] < arr[min_indx]:
                min_indx = j
                
        arr[i],arr[min_indx] = arr[min_indx],arr[i] 
    
    return arr
        

arr = [3, 5, 0, 9, 8]
n = 5
res = selection_sort(arr,n)

print(" ".join(map(str,res)))