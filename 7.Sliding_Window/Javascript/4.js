// function  subarray_sum_exists(arr, N, K){
    
//     for(let i=0;i<N;i++){
//         sum = 0
//         for(j=i;j<N;j++){
//             sum += arr[j]
//             if(sum === K){
//                 return true
//             }
//         }
//     }
//     return false
// }

// arr = [1, 2, 3, 4, 5]
// N = 5
// K = 9

// res = subarray_sum_exists(arr, N, K)
// console.log(res)

function subarraySumExists(arr, N, K) {
    let currentSum = 0;
    const sumMap = { 0: 1 }; // Initialize with sum 0 to handle subarrays starting from index 0

    for (let num of arr) {
        currentSum += num;

        if ((currentSum - K) in sumMap) {
            return "Yes";
        }

        if (currentSum in sumMap) {
            sumMap[currentSum] += 1;
        } else {
            sumMap[currentSum] = 1;
        }
    }

    return "No";
}

// Example usage
const arr = [1, 2, 3, 4, 5];
const N = 5;
const K = 9;

const res = subarraySumExists(arr, N, K);
console.log(res); // Output: "Yes"
