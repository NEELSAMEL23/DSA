function maxArea(height) {
    let left = 0;
    let right = height.length - 1;
    let maxArea = 0;
    
    while (left < right) {
        // Calculate the area with the current pair of lines
        const width = right - left;
        const area = Math.min(height[left], height[right]) * width;
        maxArea = Math.max(maxArea, area);
        
        // Move the pointer pointing to the shorter line inward
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    
    return maxArea;
}

const arr = [1, 8, 6, 2, 5, 4, 8, 3, 7];
const result = maxArea(arr);
console.log(result);






// The time complexity of the maxArea function is O(n), where n is the number of elements in the height array.

// Explanation:
// The left and right pointers start at opposite ends of the array and move towards each other in each iteration of the while loop.
// In each iteration, either left is incremented or right is decremented, so the pointers only move in one direction at a time.
// Since each element is visited only once, the total number of iterations is proportional to the size of the array, resulting in a linear time complexity of O(n).
// Thus, the time complexity of this algorithm is O(n), where n is the length of the input array.



//The space complexity of the maxArea function is O(1).

// Explanation:
// The function uses a constant amount of extra space, regardless of the size of the input array height.
// The only extra variables used are left, right, and maxArea, all of which take constant space.
// No additional data structures (like arrays or hashmaps) are created that would grow with the input size.
// Since the amount of extra space used does not depend on the size of the input array, the space complexity is O(1).