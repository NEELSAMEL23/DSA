function min(arr,N) {
    let min_val = arr[0];  // Initialize with the first element
    for (let i = 1; i < arr.length; i++) {  // Start from the second element
        if (arr[i] < min_val) {  // Compare the element, not the index
            min_val = arr[i];
        }
    }
    return min_val;  // Return the minimum value after the loop
}

let arr = [1, 2, 3, 4, 5];
console.log(min(arr));  // Output: 1


function min_arr(arr){
    return Math.min(...arr)
}

N = 5
arr = [1,2,3,4,5]
res = min_arr(arr,N)
console.log(res)