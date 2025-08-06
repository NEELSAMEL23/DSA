function twoSum(N, B, arr) {
  let left = 0;
  let right = N - 1;
  let found = false;

  while (left < right) {
    const currentSum = arr[left] + arr[right];

    if (currentSum === B) {
      console.log(left, right);
      found = true;
      break;
    } else if (currentSum < B) {
      left++;
    } else {
      right--;
    }
  }

  if (!found) { 
    return "-1 -1";
  }
}

// Example usage:
const N = 4;
const B = 9;
const arr = [2, 7, 11, 15];

const res = twoSum(N, B, arr);
console.log(res);
