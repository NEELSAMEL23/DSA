def profile_pic(L, Length, W, Width):
    if L > Length:
        print("Upload")
    else:
        print("Increase Length")

    if W > Width:
        print("Upload")
    else:
        print("Increase Length")

# Hardcoded input
L = 12
Length = 8
W = 14
Width = 19
profile_pic(L, Length, W, Width)
