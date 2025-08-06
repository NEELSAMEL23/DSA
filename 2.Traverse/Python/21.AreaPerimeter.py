def Area_Perimeter(L1, B1, L2, B2):
    Area_Triangle1 = L1 * B1
    Area_Triangle2 = L2 * B2

    Area_Perimeter1 = 2 * (L1 + B1)
    Area_Perimeter2 = 2 * (L2 + B2)

    if Area_Triangle1 > Area_Triangle2:
        print(True)
    else:
        print(False)

    if Area_Perimeter1 > Area_Perimeter2:
        print(True)
    else:
        print(False)

L1 = 1
B1 = 2
L2 = 2
B2 = 3

Area_Perimeter(L1, B1, L2, B2)
