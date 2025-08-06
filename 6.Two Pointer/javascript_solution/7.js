function lifeboatsNeeded(weights, n, k) {
    // Step 1: Sort the array in ascending order
    weights.sort((a, b) => a - b);

    let left = 0; // Pointer to the lightest person
    let right = n - 1; // Pointer to the heaviest person
    let boats = 0;

    // Step 2: Use a two-pointer approach
    while (left <= right) {
        // Check if the lightest and heaviest person can share a boat
        if (weights[left] + weights[right] <= k) {
            left++; // Move to the next lightest person
            right--; // Move to the next heaviest person
        } else {
            right--; // Only take the heaviest person in a separate boat
        }
        
        // A boat is used in either case
        boats++;
    }

    return boats;
}

// Example usage:
let arr = [3, 5, 4, 3];
let n = arr.length;
let k = 5;
console.log(lifeboatsNeeded(arr, n, k)); // Output: 4











// Time Complexity Analysis
// Sorting the array → O(nlogn)
// The sort() function in JavaScript typically uses Timsort, which runs in O(n log n).
// Two-pointer traversal → O(n)
// We iterate through the array once, moving left and right pointers towards each other.
// Each element is processed at most once, making this step O(n).
// Overall Time Complexity:- O(nlogn)+O(n)=O(nlogn)
// Sorting dominates the complexity, so the function runs in O(n log n).



// Space Complexity Analysis
// Sorting is in-place → O(1)
// JavaScript’s sort() sorts the array in place, requiring no extra space.
// Two pointers and a counter → O(1)
// We use a few integer variables (left, right, boats), which take constant space.
// Overall Space Complexity:- O(1)
// The algorithm does not use extra space apart from input storage, making it space-efficient.


// Final Complexity Summary
// Time Complexity: O(n log n)
// Space Complexity: O(1)