function findPairCount(arr, k) {
    arr.sort((a, b) => a - b); // Sort the array in ascending order
    let i = 0, j = arr.length - 1;
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

    return count;
}


arr = [3, 0, 6, 2, 7]
k = 9
const res = findPairCount(arr, k)
console.log(res)


// Time Complexity:
// Sorting the array → O(nlogn)
// Two-pointer traversal  → O(n)

// Total Time Complexity: O(nlogn)+O(n)=O(nlogn)

// Space Complexity:

// In-place sorting (JavaScript’s sort() modifies the original array) →O(1)
// No extra data structures used →O(1)
// Total Space Complexity:O(1)