function excelColumnNumber(columnTitle) {
    let columnNumber = 0;
    for (let i = 0; i < columnTitle.length; i++) {
        let charCode = columnTitle.charCodeAt(i) - 'A'.charCodeAt(0) + 1;
        columnNumber = columnNumber * 26 + charCode;
    }
    return columnNumber;
}

// Example usage
let columnTitle = "AB";
// columnTitle = "ZY";  // You can test with different titles
let res = excelColumnNumber(columnTitle);
console.log(res);  // Output: 28 for "AB", 701 for "ZY"
