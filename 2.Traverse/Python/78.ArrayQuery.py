def array_query(arr, N, Q, queries):
    for i in range(Q):
        found = False
        for j in range(N):
            if arr[j] == queries[i]:
                found = True
                break
        if found:
            print("YES")
        else:
            print("NO")

arr = [1, 2, 3, 4, 5]
N = 5
Q = 3
queries = [3, 5, 7]

array_query(arr, N, Q, queries)
