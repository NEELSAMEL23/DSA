def second_maximum(a, b, c):
    if (a > b and a < c) or (a > c and a < b):
        print(a)
    elif (b > a and b < c) or (b > c and b < a):
        print(b)
    else:
        print(c)

a = 3
b = 7
c = 5

second_maximum(a, b, c)
