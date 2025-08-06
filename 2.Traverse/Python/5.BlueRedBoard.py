def last_painted_color(board):
    for row in board:
        if row == "RRRRRRRR":
            return 'R'
    return 'B'

# Hardcoded single board input
board = [
    "BBBBBBBB",
    "BBBBBBBB",
    "BBBBBBBB",
    "BBBBBBBB",
    "BBBBBBBB",
    "BBBBBBBB",
    "BBBBBBBB",
    "RRRRRRRR"
]

print(last_painted_color(board))
