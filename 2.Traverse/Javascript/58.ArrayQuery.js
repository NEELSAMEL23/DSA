function arrayQuery(arr, queries) {
    for (let i = 0; i < queries.length; i++) {
        let found = false;

        for (let j = 0; j < arr.length; j++) {
            if (arr[j] === queries[i]) {
                found = true;
                break;
            }
        }

        if (found) {
            console.log("YES");
        } else {
            console.log("NO");
        }
    }
}

// 🔽 Single hardcoded input
const arr = [1, 2, 3, 4, 5];
const queries = [3, 5, 7];

// Run
arrayQuery(arr, queries);
