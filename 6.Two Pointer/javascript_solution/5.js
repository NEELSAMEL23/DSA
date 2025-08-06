function pairLessThanK(arr, k) {
    arr.sort((a, b) => a - b); // Sort the array in ascending order
    let i = 0;
    let j = arr.length - 1;
    let maxPair = -1;

    while (i < j) {
        let current = arr[i] + arr[j];

        if (current < k) {
            maxPair = Math.max(maxPair, current);
            i++; // Move left pointer forward
        } else {
            j--; // Move right pointer backward
        }
    }
    return maxPair;
}

// Test cases
let k = 7;
let arr1 = [1, 2, 3, 4, 5]; 
console.log(pairLessThanK(arr1, k));

let arr2 = [15, 2, 30];
console.log(pairLessThanK(arr2, k)); 


// Expected output: 6
// Expected output: -1








// time complexity 
// 1. Sorting the array:arr.sort((a, b) => a - b) takes O(n log n) time.
// 2. Two-pointer traversal:The while loop runs at most O(n) times because each iteration either increments i or decrements j.
// 3.Overall Complexity:Since sorting dominates, the overall time complexity is O(n log n).

// Space Complexity
// O(1) (constant space) since the sorting is done in place and only a few extra variables are used.