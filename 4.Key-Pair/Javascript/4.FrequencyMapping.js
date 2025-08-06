function frequencyMap(arr) {
  const map = {};
  for (let item of arr) {
    map[item] = (map[item] || 0) + 1;
  }
  return map;
}

// Example
let arr = ["apple", "banana", "apple", "orange", "banana"]
console.log(frequencyMap(arr));
// Output: { apple: 2, banana: 2, orange: 1 }
