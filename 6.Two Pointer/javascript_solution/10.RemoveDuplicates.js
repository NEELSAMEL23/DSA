function removeDuplicates(arr) {


  let i = 1; // position to insert next allowed element
  let count = 1; // count of current element occurrences

  for (let j = 1; j < arr.length; j++) {
    if (arr[j] === arr[j - 1]) {
      count++;
    } else {
      count = 1;
    }

    if (count <= 2) {
      arr[i] = arr[j];
      i++;
    }
  }

  return { result: arr.slice(0, i), length: i };
}

// Example usage:
const arr = [1,1,1,1,3,3,3,3,4,6,6,6,6,6,6,7];
const { result, length } = removeDuplicates(arr);

console.log(result);
console.log(length);
