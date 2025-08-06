function areAnagrams(str1, str2) {
    // Step 1: Remove spaces and convert to lowercase
    str1 = str1.replace(/\s+/g, "").toLowerCase();
    str2 = str2.replace(/\s+/g, "").toLowerCase();

    // Step 2: If lengths differ, not anagrams
    if (str1.length !== str2.length) return false;

    // Step 3: Count characters in str1
    let charCount = {};

    for (let char of str1) {
        charCount[char] = (charCount[char] || 0) + 1;
    }

    // Step 4: Subtract counts based on str2
    for (let char of str2) {
        if (!charCount[char]) {
            return false; // Either char not found or extra in str2
        }
        charCount[char]--;
    }

    // Step 5: All counts should be zero (optional final check)
    return true;
}

// ✅ Example:
console.log(areAnagrams("anagram", "nag a ram")); // true
console.log(areAnagrams("listen", "silent"));     // true
console.log(areAnagrams("hello", "world"));       // false
