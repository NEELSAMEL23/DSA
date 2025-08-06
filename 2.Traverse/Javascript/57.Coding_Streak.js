function codingStreak(logs) {
    let maxContinuousC = 0;  // X
    let maxTotalCInDay = 0;  // Y

    for (let log of logs) {
        let currStreak = 0;
        let maxStreakInDay = 0;
        let totalC = 0;

        for (let char of log) {
            if (char === 'C') {
                currStreak++;
                totalC++;
                maxStreakInDay = Math.max(maxStreakInDay, currStreak);
            } else {
                currStreak = 0;
            }
        }

        maxContinuousC = Math.max(maxContinuousC, maxStreakInDay);
        maxTotalCInDay = Math.max(maxTotalCInDay, totalC);
    }

    console.log(maxContinuousC, maxTotalCInDay);
}



// Sample input
const logs = [
    "SSSSEEEECCCCEECCCC",
    "CCCCCSSSSEEECCCCSS",
    "SSSSSEEESSCCCCCCCS",
    "EESSSSCCCCCSSEEEE"
];

codingStreak(logs);
