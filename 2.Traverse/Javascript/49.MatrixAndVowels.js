function findVowels(arr, N, M) {
    const vowels = "aeiou";

    for (let col = 0; col < M; col++) {
        let vowelsPresent = false;

        for (let row = 0; row < N; row++) {
            if (vowels.includes(arr[row][col])) {
                vowelsPresent = true;
                break;
            }
        }

        if (vowelsPresent) {
            console.log("Yes");
        } else {
            console.log("No");
        }
    }
}

// Example input
const arr = [
    ["l", "m", "n"],
    ["o", "p", "q"],
    ["r", "s", "t"]
];

const N = 3;
const M = 3;

findVowels(arr, N, M);
