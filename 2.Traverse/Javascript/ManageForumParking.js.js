function isParkingPossible(k, arrival, departure) {
    const events = [];

    for (let i = 0; i < arrival.length; i++) {
        events.push([arrival[i], 1]);    // Car arrives
        events.push([departure[i], -1]); // Car departs
    }

    // Sort events: first by time, then departure before arrival if equal
    events.sort((a, b) => {
        if (a[0] === b[0]) return a[1] - b[1];
        return a[0] - b[0];
    });

    let currentCars = 0;

    for (let [_, event] of events) {
        currentCars += event;
        if (currentCars > k) {
            return "Not Possible";
        }
    }

    return "Possible";
}

// 🔽 Hardcoded Input
const k = 1;
const arrival = [1, 3, 5];
const departure = [2, 6, 8];

console.log(isParkingPossible(k, arrival, departure));  // Output: Possible
