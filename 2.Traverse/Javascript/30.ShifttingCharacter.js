function shiftingCharacters(n, s, k) {
    let result = [];

    for (let i = 0; i < s.length; i++) {
        let char = s[i];
        let newChar = String.fromCharCode(
            ((char.charCodeAt(0) - 'a'.charCodeAt(0) + k) % 26) + 'a'.charCodeAt(0)
        );
        result.push(newChar);
    }

    return result.join('');
}

// Hardcoded input
let n = 5;
let s = "abz";
let k = 2;

let res = shiftingCharacters(n, s, k);
console.log(res);  // Output: "cdb"
