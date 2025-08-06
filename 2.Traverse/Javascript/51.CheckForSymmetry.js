function isHorizontalSymmetric(matrix, n, m){
    
    for(let i=0;i<Math.floor(n/2);i++){
        if(JSON.stringify(matrix[i])!==JSON.stringify(matrix[n-i-1])){
            return false
        }
    }
    
    return true
    
}


function isVerticalSymmetric(matrix, n, m) {
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < Math.floor(m / 2); j++) {
            if (matrix[i][j] !== matrix[i][m - j - 1]) {
                return false;
            }
        }
    }
    return true;
}


const n = 4;
const m = 3;
const matrix = [
    ["*", "*", "."],
    [".", ".", "*"],
    [".", ".", "*"],
    ["*", "*", "."],
];

const horizontal = isHorizontalSymmetric(matrix, n, m);
const vertical = isVerticalSymmetric(matrix, n, m);

if (horizontal && vertical) {
    console.log("BOTH");
} else if (horizontal) {
    console.log("HORIZONTAL");
} else if (vertical) {
    console.log("VERTICAL");
} else {
    console.log("NO");
}

