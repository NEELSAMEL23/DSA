def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '_':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '_':
            return board[0][i]


    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        return board[0][2]

    return "Tie"


board = [
    ["x","o","x"],["o","x","x"],["x","x",'x']
    ]
result = check_winner(board)
if result == 'x':
    print('x')
elif result == 'o':
    print('o')
else:
    print('Tie')  