function findPairCount(arr, k) {
    arr.sort((a, b) => a - b);  // Sort the array in ascending order
    let i = 0;
    let j = arr.length - 1;
    let count = 0;

    while (i < j) {
        if (arr[i] + arr[j] === k) {
            count++;
            i++;
            j--;
        } else if (arr[i] + arr[j] < k) {
            i++;
        } else {
            j--;
        }
    }

    return count > 0 ? count : -1;
}

let arr = [3, 4, 0, 2, 7];
let k = 2;
let result = findPairCount(arr, k);
console.log(result);




// Time complexity 
// Step 1
// Sorting the array:
// The array is sorted with the line arr.sort((a, b) => a - b);.
// The time complexity of the sort operation is O(n log n), where n is the number of elements in the array.

// Step 2
// Two-pointer traversal:
// After sorting, you traverse the array using two pointers (i and j), moving them inward until they meet. In each iteration of the while loop, either i is incremented or j is decremented, meaning each pointer moves at most n times.
// This traversal takes O(n) time.


// Overall Time Complexity:
// Sorting takes O(n log n).
// The two-pointer traversal takes O(n).

// Thus, the overall time complexity of the findPairCount function is:
// O(n log n) + O(n) = O(n log n)
// Therefore, the time complexity of the function is O(n log n).













//Space Complexity

// Two-Pointer Approach (Your Code)
// arr.sort((a, b) => a - b);  // Sorting in-place
// Sorting is done in-place, meaning it does not require extra space.
// Variables i, j, count use O(1) space.
// No additional data structures are used.


// Total Space Complexity:
// O(1) (Constant space)