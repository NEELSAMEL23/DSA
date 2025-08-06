function findGreaterElements(arr, n) {
    let maxFromRight = arr[n - 1];
    let result = [maxFromRight];

    for (let i = n - 2; i >= 0; i--) {
        if (arr[i] >= maxFromRight) {
            result.push(arr[i]);
            maxFromRight = arr[i];
        }
    }

    return result.reverse();
}

const n = 6;
const arr = [16, 17, 4, 3, 5, 2];

const res = findGreaterElements(arr, n);
console.log(...res);
