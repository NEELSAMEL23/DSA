def pow(a,b):
    if b == 0:
        return 1
    else:
        return a * pow(a,b-1)

a = 2
b = 4
res = pow(a,b)
print(res)


