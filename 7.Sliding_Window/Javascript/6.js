function longestSubstring(s, k) {
    const n = s.length;
    let maxLen = 0;

    // Iterate through all possible substrings
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j <= n; j++) {
            // Step 1: Get the substring
            const substring = s.slice(i, j);

            // Step 2: Create a dictionary to store character counts
            const charCounts = {};
            for (let char of substring) {
                if (charCounts[char]) {
                    charCounts[char]++;
                } else {
                    charCounts[char] = 1;
                }
            }

            // Step 3: Check if every character appears at least k times
            let valid = true;
            for (let count of Object.values(charCounts)) {
                if (count < k) {
                    valid = false;
                    break;
                }
            }

            // Step 4: Update maxLen if valid
            if (valid) {
                maxLen = Math.max(maxLen, j - i);
            }
        }
    }

    return maxLen;
}

// Example usage
const s = "aaabb";
const k = 3;
const res = longestSubstring(s, k);
console.log(res); // Output: 3
