function countSubstringsWithKDistinctBruteforce(s, n, k) {
    let count = 0;
    
    // Iterate over all possible starting points
    for (let start = 0; start < n; start++) {
        // Create a set to keep track of distinct characters
        let distinctChars = new Set();
        
        // Iterate over all possible ending points
        for (let end = start; end < n; end++) {
            distinctChars.add(s[end]);
            
            // If the number of distinct characters is equal to k, increment the count
            if (distinctChars.size === k) {
                count++;
            }
            // If the number of distinct characters exceeds k, break the loop
            else if (distinctChars.size > k) {
                break;
            }
        }
    }
    
    return count;
}

const s = "abcc";
const n = 4;
const k = 2;

const result = countSubstringsWithKDistinctBruteforce(s, n, k);
console.log(result);
