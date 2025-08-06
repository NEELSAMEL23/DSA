function leftRightIntersection(N,S) {


  const A = [0];

  for (let i = 1; i <= N; i++) {
    const pos = A.indexOf(i - 1);

    if (S[i - 1] === 'L') {
      A.splice(pos, 0, i); // insert i at pos
    } else {
      A.splice(pos + 1, 0, i); // insert i at pos + 1
    }
  }

  return A.join(" ");
}

// 🔽 Hardcoded input
const N = 5;
const S = "RLRLR";

// Run the function
res= leftRightIntersection(N,S);
console.log(res)