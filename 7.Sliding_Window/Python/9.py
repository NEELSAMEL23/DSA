def max_families_within_diversity_bruteforce(income, n, k):
    income.sort()  # Sort the income list first
    max_families = 1  # At least one family in the worst case

    for i in range(n):
        min_income = income[i]
        max_income = income[i]

        for j in range(i, n):
            min_income = min(min_income, income[j])
            max_income = max(max_income, income[j])

            # If the difference between max and min income is within k
            if max_income - min_income <= k:
                max_families = max(max_families, j - i + 1)

    return max_families

    

income = [20, 15, 30, 10, 25]
n = 5
k = 10
res = max_families_within_diversity_bruteforce(income, n, k)
print(res)







def max_families_within_diversity(income, n, k):
    income.sort()  
    
    left = 0
    max_families = 1
    
    for right in range(1, n):

        while income[right] - income[left] > k:
            left += 1
                                                                                    
        max_families = max(max_families, right - left + 1)
    
    return max_families


income = [20, 15, 30, 10, 25]
n = 5
k = 10
res = max_families_within_diversity_bruteforce(income, n, k)
print(res)
