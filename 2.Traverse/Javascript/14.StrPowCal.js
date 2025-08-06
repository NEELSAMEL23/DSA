function strPowCal(str) {
    const vowels = "AEIOUaeiou";
    let X = 0;
    let Y = 0;

    for (let i = 0; i < str.length; i++) {
        if (vowels.includes(str[i])) {
            X += 1;
        } else {
            Y += 1;
        }
    }

    let cal = 3 * X + 5 * Y;
    return cal;
}

// Hardcoded input
let N = 4;
let inputStr = "aman";
let res = strPowCal(inputStr);
console.log(res);
