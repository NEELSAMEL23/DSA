tc = int(input())

arr = list(map(int,input().split()))

array = [int(i)+1 for i in arr]

print(*array)

# input:- 5
#         1 2 3 4 5
    
# output:- 2 3 4 5 6