function solve(a, b, c, d) {
    if ((b - a === c - b) && (c - b === d - c)) {
        console.log("Arithmetic");
    } else if ((b / a === c / b) && (c / b === d / c)) {
        console.log("Geometric");
    } else {
        console.log("Neither");
    }
}

// Example usage
solve(2, 4, 6, 8);    // Arithmetic
solve(2, 6, 18, 54);  // Geometric
solve(1, 2, 4, 9);    // Neither
