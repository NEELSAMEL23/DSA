function isPalindrome(s) {
    let i = 0;
    let j = s.length - 1;

    while (i < j) {
        while (i < j && !isAlphanumeric(s[i])) i++

        while (i < j && !isAlphanumeric(s[j])) j--
        

        if (s[i].toLowerCase() !== s[j].toLowerCase()) {
            return false;
        }

        i++;
        j--;
    }

    return true;
}

// Helper function to check if a character is alphanumeric
function isAlphanumeric(char) {
    return /[a-zA-Z0-9]/.test(char);
}

// Example usage:
 const S = "MOM";
console.log(isPalindrome(S));// Output: true





// Time Complexity Analysis of isPalindrome Function
// The function processes each character in the input string at most once using a two-pointer approach (i and j). Let's break it down:
// Skipping Non-Alphanumeric Characters
// The while loops move i and j forward or backward when encountering non-alphanumeric characters.
// In the worst case (if the string has mostly non-alphanumeric characters), both i and j traverse the entire string.
// Comparing Characters
// Each valid alphanumeric character is compared once.
// Since every character is processed at most once, the overall time complexity is:O(n)


// Space Complexity
// We only use a few extra variables (i, j) and a helper function for character checking.
// No extra data structures are used, so the space complexity is:O(1)