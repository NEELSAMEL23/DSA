function ancientTreasureHunt(gems, n) {

    let i = 0;
    let j = n - 1;

    let leftSum = 0;
    let rightSum = 0;    

    let maxGems = 0;


    while (i <= j) {
        if (leftSum === rightSum) {
            maxGems = leftSum;
        }

        if (leftSum <= rightSum) {
            leftSum += gems[i];
            i++;
        } else {
            rightSum += gems[j];
            j--;
        }


    }

    console.log(maxGems);
}

    const gems = [5, 2, 5, 2, 1, 4, 6, 6]; // change as needed
    const n = gems.length;
    // Call the function
    ancientTreasureHunt(gems, n);
