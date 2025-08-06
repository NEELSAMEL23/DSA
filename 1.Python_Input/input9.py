tc = int(input())

for i in range(tc):
    
    n = int(input())
    
    matrix = []
            
    for i in range(n):
        arr = [int(num)+1 for num in input().split()]
        matrix.append(arr)
        
    for row in matrix:
            print(' '.join(map(str, row)))

# input:-
# 2
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# 2
# 1 2
# 3 4

# output:- 
# 2 3 4
# 5 6 7
# 8 9 10
# 2 3
# 4 5