for (let i = 1; i <= 5; i++) {
  if (i == 3) {
    continue;
  } else {
    let row = " ";
    for (let j = 1; j <= i; j++) {
      if (j == 3) {
        continue;
      } else if (j % 7 == 0) {
        break;
      } else {
        row += j + " ";
      }
    }
    console.log(row.trim());
  }
}
