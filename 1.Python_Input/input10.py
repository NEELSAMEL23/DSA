N, M = map(int, input().split())

matrix = []

for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)


for i in range(N):
    for j in range(M):
        matrix[i][j] += 1
        print(matrix[i][j], end=' ')
    print()  

# Input:-
# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

# output:- 
# 2 3 4 5
# 6 7 8 9
# 10 11 12 13