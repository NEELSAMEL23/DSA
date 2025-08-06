def GCD(a,b):

    if b == 0:
        return a
    else:
        return GCD(b,a%b)


a = 6
b = 9
res = GCD(a,b)
print(res)