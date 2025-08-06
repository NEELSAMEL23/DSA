function mergeSortedArrays(arr1, arr2) {
    // Ensure arrays are sorted before merging
    arr1.sort((a, b) => a - b);
    arr2.sort((a, b) => a - b);

    let i = 0, j = 0;
    let mergedArray = [];

    // Merge both arrays
    while (i < arr1.length && j < arr2.length) {
        if (arr1[i] < arr2[j]) {
            mergedArray.push(arr1[i]);
            i++;
        } else if (arr1[i] > arr2[j]) {
            mergedArray.push(arr2[j]);
            j++;
        } else {  // If elements are equal, push both and move both pointers
            mergedArray.push(arr1[i]);
            mergedArray.push(arr2[j]);
            i++;
            j++;
        }
    }

    // Add remaining elements of arr1 (if any)
    while (i < arr1.length) {
        mergedArray.push(arr1[i++]);
    }

    // Add remaining elements of arr2 (if any)
    while (j < arr2.length) {
        mergedArray.push(arr2[j++]);
    }

    return mergedArray;
}   

// Test Cases
let arr1 = [3, 1, 2];
let arr2 = [5, 4, 3, 2];

let res = mergeSortedArrays(arr1, arr2);
console.log(res);  // Output: [1, 2, 2, 3, 3, 4, 5]











// Time Complexity:
// The time complexity of the mergeSortedArrays function consists of two major parts:

// Sorting the arrays:
// Sorting each of the arrays arr1 and arr2 takes O(n log n) time where n is the length of the array. In the worst case, if both arrays have lengths n1 and n2, sorting them individually will take O(n1 log n1) and O(n2 log n2) respectively.

// Merging the two arrays:
// The merging process involves iterating through both arrays once and comparing their elements, which takes O(n1 + n2) time, where n1 is the length of arr1 and n2 is the length of arr2.


// So, the overall time complexity is dominated by the sorting step, which is O(n log n), where n = max(n1, n2).
// Thus, the time complexity of the entire function is: O(n1 log n1 + n2 log n2) (Sorting time) + O(n1 + n2) (Merging time)
// In the worst case, this simplifies to: O((n1 + n2) log(n1 + n2)).



// Space Complexity:
// The space complexity is primarily determined by the space used for the merged array.
// Space for sorted arrays: Sorting the arrays does not require extra space since the .sort() method in JavaScript sorts the array in-place. So, no additional space is used for sorting.
// Space for the merged array: The mergedArray will store all the elements from both arrays, so its size will be n1 + n2. Therefore, the space complexity is O(n1 + n2) for storing the merged result.
// Thus, the space complexity is: O(n1 + n2).