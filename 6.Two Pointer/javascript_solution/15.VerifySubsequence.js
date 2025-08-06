function verifySubsequence(s, t) {
    let i = 0
    let j = 0;

    
    while (i < s.length && j < t.length) {
        if (s[i] === t[j]) {
            i++;
        }
        j++;
    }

    if (i === s.length) {
        console.log("true");
    } else {
        console.log("false");
    }
}

let s = "abc";
let t = "ahbgdc";
verifySubsequence(s, t);
