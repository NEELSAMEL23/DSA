let n = 5;
for (let i = n; i >= 1; i--) {
  let store = "";
  for (let j = 1; j <= i; j++) {
    store += "*" + ' ';
  }
  console.log(store);
}
