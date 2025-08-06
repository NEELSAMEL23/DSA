function rainWaterTrapped(arr, n) {
    let left = 0 
    let right = n - 1;

    let leftMax = 0
    let rightMax = 0;
    
    let result = 0;

    while (left <= right) {
        
        if (arr[left] <= arr[right]) {
            
            if (arr[left] >= leftMax) {
                leftMax = arr[left];
            } else {
                result += leftMax - arr[left];
            }
            left++;
        } else {
            if (arr[right] >= rightMax) {
                rightMax = arr[right];
            } else {
                result += rightMax - arr[right];
            }
            right--;
        }
    }
    return result;
}
 
// ✅ Hardcoded single input
let arr = [7, 0, 3, 6, 2, 3, 5];
let n = arr.length;

console.log(rainWaterTrapped(arr, n)); // Output: 14
