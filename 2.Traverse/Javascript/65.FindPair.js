function maxSumPair(arr) {
  if (arr.length < 2) return null;
  let max1 = -Infinity, max2 = -Infinity;

  for (let num of arr) {
    if (num > max1) {
      max2 = max1;
      max1 = num;
    } else if (num > max2) {
      max2 = num;
    }
  }

  return [max1, max2];
}

// Example
let arr = [3, 5, 1, 7, 9]
console.log(maxSumPair(arr)); // Output: [9, 7]
