function arrangeMedals(n, participants) {
    let count_gold = 0;
    let count_silver = 0;
    let count_bronze = 0;

    // Count each medal type
    for (let medal of participants) {
        if (medal === 0) {
            count_gold++;
        } else if (medal === 1) {
            count_silver++;
        } else {
            count_bronze++;
        }
    }

    // Build sorted result: Golds (0), then Silvers (1), then Bronzes (2)
    const result = [
        ...Array(count_gold).fill(0),
        ...Array(count_silver).fill(1),
        ...Array(count_bronze).fill(2)
    ];

    return result;
}

// 🔽 Hardcoded input
const participants = [2, 0, 1];
const n = participants.length;

const res = arrangeMedals(n, participants);
console.log(...res);  // Output: 0 1 2
