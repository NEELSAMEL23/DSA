function checkWinner(board) {
    for (let i = 0; i < 3; i++) {
        // Check rows
        if (board[i][0] === board[i][1] && board[i][1] === board[i][2] && board[i][0] !== '_') {
            return board[i][0];
        }

        // Check columns
        if (board[0][i] === board[1][i] && board[1][i] === board[2][i] && board[0][i] !== '_') {
            return board[0][i];
        }
    }

    // Check diagonals
    if (board[0][0] === board[1][1] && board[1][1] === board[2][2] && board[0][0] !== '_') {
        return board[0][0];
    }

    if (board[0][2] === board[1][1] && board[1][1] === board[2][0] && board[0][2] !== '_') {
        return board[0][2];
    }

    return "Tie";
}

const board = [
    ['x', 'o', 'x'],
    ['o', 'x', 'x'],
    ['x', 'x', 'x']
];

const result = checkWinner(board);

if (result === 'x') {
    console.log('x');
} else if (result === 'o') {
    console.log('o');
} else {
    console.log('Tie');
}
