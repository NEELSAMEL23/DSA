def odd_even_both(one, two):
    if one % 2 == 0 and two % 2 == 0:
        print("Even")
    elif one % 2 != 0 and two % 2 != 0:
        print("Odd")
    else:
        print("Even-Odd")

# Example call
odd_even_both(2, 3)
