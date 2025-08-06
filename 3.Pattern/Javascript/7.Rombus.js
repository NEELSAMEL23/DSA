let n = 5; // Number of rows for the upper half

for (let i = 0; i <= 2 * n; i++) {
  let res = "";

  // Determine current row index (mirror for lower part)
  let current = i <= n ? i : 2 * n - i;

  // Adding spaces
  for (let j = 0; j < n - current; j++) {
    res += "  ";
  }

  // Increasing numbers
  for (let j = 0; j <= current; j++) {
    res += j + " ";
  }

  // Decreasing numbers
  for (let j = current - 1; j >= 0; j--) {
    res += j + " ";
  }

  console.log(res);
}
