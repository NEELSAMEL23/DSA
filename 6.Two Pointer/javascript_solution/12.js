function tripleSum(arr, n) {
    // Step 1: Sort the array
    arr.sort((a, b) => a - b);  // Sorting in ascending order

    // Step 2: Fix one element and use two pointers for the remaining two elements
    for (let k = n - 1; k >= 2; k--) {  // Iterate over possible third elements
        let i = 0;
        let j = k - 1;

        while (i < j) {
            let sumPair = arr[i] + arr[j];
            if (sumPair === arr[k]) {
                return 1;  // Triplet found
            } else if (sumPair < arr[k]) {
                i++;  // Increase the sum by moving left pointer to the right
            } else {
                j--;  // Decrease the sum by moving right pointer to the left
            }
        }
    }
    return 0;  // No triplet found
}

// Test the function
let arr = [7, 1, 2, 9, 4, 8, 6, 5];
let n = arr.length;  // Length of the array
let result = tripleSum(arr, n);
console.log(result);  // Output: 1













// Time Complexity Analysis
// The function follows these steps:
// Sorting the Array
// Sorting takes O(n log n) time.
// Iterating Over the Array
// The outer loop runs from k = n - 1 to k = 2, which means it runs O(n) times.
// Two-Pointer Approach
// For each value of k, we use two pointers (i and j) to check for a valid pair, which takes O(n) time in the worst case.
// So, the overall time complexity is: O(nlogn)+O(n^2)=O(n^2)



//The space complexity is O(1) (constant space).