tc = int(input())

matrix = []
        
for i in range(tc):
    arr = [int(num)+1 for num in input().split()]
    matrix.append(arr)
    
for row in matrix:
        print(' '.join(map(str, row)))

# Input:-
# 3 
# 1 2 3
# 4 5 6
# 7 8 9

# output:- 
# 2 3 4
# 5 6 7
# 8 9 10