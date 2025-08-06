function solve(n, m) {
  for (let i = 0; i < n; i++) {
    if (i % 2 === 0) {
      console.log('#'.repeat(m));
    } else if (i % 4 === 1) {
      console.log('.'.repeat(m - 1) + '#');
    } else {
      console.log('#' + '.'.repeat(m - 1));
    }
  }
}

solve(3,3)