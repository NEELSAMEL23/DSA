function lastPaintedColor(board) {
    for (let row of board) {
        if (row === "RRRRRRRR") {
            return 'R';
        }
    }
    return 'B';
}

// Hardcoded single board input
const board = [
    "....B....",
    "....B....",
    "....B....",
    "RRRRRRRR",
    "....B....",
    "....B....",
    "....B....",
    "....B....",

];

console.log(lastPaintedColor(board));
