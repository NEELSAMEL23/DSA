function arePermutations(s1, s2) {
    if (s1.length !== s2.length) {
        console.log("No");
        return;
    }

    const charCount = {};

    // Count characters in s1
    for (let ch of s1) {
        if (charCount[ch]) {
            charCount[ch]++;
        } else {
            charCount[ch] = 1;
        }
    }

    // Subtract character counts using s2
    for (let ch of s2) {
        if (!charCount[ch] || charCount[ch] === 0) {
            console.log("No");
            return;
        }
        charCount[ch]--;
    }

    console.log("Yes");
}

// Input
const s1 = "amit";
const s2 = "mtia";

arePermutations(s1, s2);
