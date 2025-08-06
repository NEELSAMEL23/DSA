function socks(arr) {
    arr.sort((a, b) => a - b); // Correct numeric sorting
    let i = 0;
    let totalPairs = 0;
    
    while (i < arr.length - 1) {
        if (arr[i] === arr[i + 1]) {
            totalPairs++;
            i += 2;  // Skip the next element (since it forms a pair)
        } else {
            i += 1;  // Only move one step when no pair is found
        }
    }
    return totalPairs;
}

let arr = [4, 1, 7, 4, 1, 4];
let result = socks(arr);
console.log(result);  // Output: 2 ✅


// Two-Pointer Approach:
// Time Complexity: O(nlogn), due to the sorting step.
// Space Complexity: O(1), no additional space other than the input list.