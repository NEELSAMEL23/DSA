function reversed_vowels(s) {
    let vowels = "aeiouAEIOU";
    let arr = s.split("");
    let i = 0;
    let j = s.length - 1;
    
    while (i < j) {
        while (i < j && !vowels.includes(arr[i])) i++;
        while (i < j && !vowels.includes(arr[j])) j--;

        if (i < j) {
            [arr[i], arr[j]] = [arr[j], arr[i]]; // Correct swapping
            i++;
            j--;
        }
    }
    
    return arr.join(""); // Convert array back to string
}

let s = "Hello World";
let res = reversed_vowels(s);
console.log(res); // Output: "Hollo Werld"








// 1.Time Complexity Analysis of reversed_vowels(s)
// let arr = s.split("");
// This takes O(n) time because it creates an array of characters from the string.


// 2. Two-pointer traversal    
// while (i < j) {
//     while (i < j && !vowels.includes(arr[i])) i++;
//     while (i < j && !vowels.includes(arr[j])) j--;
//     if (i < j) {
//         [arr[i], arr[j]] = [arr[j], arr[i]];
//         i++;
//         j--;
//     }
// }
// Each while loop moves either i forward or j backward until they meet.
// Each character is processed at most once.
// The total number of operations is at most O(n) since each index is visited at most twice (once moving i, once moving j).


// 3. Joining the array back into a string
// return arr.join("");
//This takes O(n) time.

// Final Complexity
//Splitting: 𝑂(𝑛)
//Two-pointer traversal: 𝑂(𝑛)
//Joining:𝑂(𝑛)
// Since all operations are O(n), the overall time complexity is:
// 𝑂 (𝑛)


// Space Complexity
// The function creates an array (arr) of size n → O(n).
// A fixed-size vowels string (constant space) → O(1).
// Thus, the space complexity is O(n) due to the extra array storage.






// Step 1: What Takes Up Space in Our Function?
// There are two main sources of memory usage:

// Input storage – This is the array itself, which is already given as input. We do not count this towards extra space because it's provided by the user.

// Extra memory usage – Any additional variables, data structures, or function calls that the program uses.


