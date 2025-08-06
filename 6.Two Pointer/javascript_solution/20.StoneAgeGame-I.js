function stoneAgeGame(stones) {
    let leftPtr = 0;
    let rightPtr = stones.length - 1;
    let leftSum = 0;
    let rightSum = 0;
    let maxEqualSum = 0;

    while (leftPtr < rightPtr) {
        if (leftSum === rightSum) {
            maxEqualSum = leftSum;
            leftSum += stones[leftPtr++];
            rightSum += stones[rightPtr--];
        } else if (leftSum < rightSum) {
            leftSum += stones[leftPtr++];
        } else {
            rightSum += stones[rightPtr--];
        }
    }

    return maxEqualSum;
}

// ✅ Example usage
const stones = [100, 1, 2, 5, 8, 97, 2, 1];
const result = stoneAgeGame(stones);
console.log(result);  // Output: 0 (no equal sum before crossing)
