tc = int(input())

def find(arr,n):
    for i in arr:
        print(i+1,end=" ")
        
for i in  range(tc):
    n = int(input())
    arr = [int(num) for num in input().split(" ")]
    find(arr,n)
    print()

# input:- 
# 2
# 5
# 1 2 3 4 5
# 4
# 1 2 3 4
# output:-
# 1 2 3 4 5
# 1 2 3 4