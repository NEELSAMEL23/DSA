def first_negative_in_window(arr, n, k):
    negative_indices = [] 
    result = []

   
    for i in range(k):
        if arr[i] < 0:
            negative_indices.append(i)

  
    if negative_indices:
        result.append(arr[negative_indices[0]])
    else:
        result.append(0)

    
    for i in range(k, n):
        
        if negative_indices and negative_indices[0] <= i - k:
            negative_indices.pop(0)

       
        if arr[i] < 0:
            negative_indices.append(i)

       
        if negative_indices:
            result.append(arr[negative_indices[0]])
        else:
            result.append(0)

    return result


def process_test_cases():
    t = int(input())  
    for _ in range(t):
        n, k = map(int, input().split())  
        arr = list(map(int, input().split())) 
        result = first_negative_in_window(arr, n, k)
        print(" ".join(map(str, result)))


process_test_cases()
