def get_bit(n, k):
    if n == 1:
        return '0'
    
    mid = 2 ** (n - 1)
    
    if k == mid:
        return '1'
    elif k < mid:
        return get_bit(n - 1, k)
    else:
        # Mirror position in S_{n-1}
        mirrored_k = 2 ** n - k
        return '1' if get_bit(n - 1, mirrored_k) == '0' else '0'
