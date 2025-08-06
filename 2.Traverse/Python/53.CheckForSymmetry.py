
def is_horizontal_symmetric(matrix, n,m):
    for i in range(n // 2):
        if matrix[i] != matrix[n - i - 1]:
            return False
    return True

def is_vertical_symmetric(matrix, n,m):
    for i in range(n):
        for j in range(n // 2):
            if matrix[i][j] != matrix[i][n - j - 1]:
                return False
    return True


n = 4
m = 3
matrix = [
    [".",".","*"],
    ["*","*","."],
    [".",".","*"],
    ["*","*","."],
]

horizontal = is_horizontal_symmetric(matrix, n,m)
vertical = is_vertical_symmetric(matrix, n,m)

if horizontal and vertical:
    print("BOTH")
elif horizontal:
    print("HORIZONTAL")
elif vertical:
    print("VERTICAL")
else:
    print("NO")

