def count_zero(n):

    if n ==0:
        return 1
    elif n<1:
        return 0
    else:
        return count_zero(n-1)+count_zero(n-2)+count_zero(n-5)

n = 4
res = count_zero(n)
print(res)