def str_length(S):

    if S == "":
        return 0
    else:
        return 1 + str_length(S[1:])


S = "Masaischool"
res = str_length(S)
print(res)