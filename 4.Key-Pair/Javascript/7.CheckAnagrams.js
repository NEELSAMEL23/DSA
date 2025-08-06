




function areAnagrams(str1, str2) {
  if (str1.length !== str2.length) return false;

  const count = {};

  for (let char of str1.toLowerCase()) {
    count[char] = (count[char] || 0) + 1;
  }

  for (let char of str2.toLowerCase()) {
    if (!count[char]) {
      return false; // char not found or count is zero
    }
    count[char]--;
  }

  return true;
}

// Example
console.log(areAnagrams("listen", "silent")); // true

