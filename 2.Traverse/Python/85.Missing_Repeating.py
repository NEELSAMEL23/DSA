def  missing_repeating(arr,n):

    total_sum = n * (n+1)/2
    total_square = n*(n+1) * (2*n+1) / 6

    actual_sum = sum(arr) 
    actual_square = sum(i*i for i in arr)
    
    diff_sum = total_sum - actual_sum
    diff_square = total_square - actual_square

    missing = int((diff_sum + diff_square/diff_sum)/2)
    repeating = int(missing - diff_sum)

    print(missing,repeating)


n = 5
arr = [1, 2, 3, 3, 4]
missing_repeating(arr,n)
