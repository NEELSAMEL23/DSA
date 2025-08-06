function canSortTrucks(trucks, n) {
    const sideLane = [];
    let current = 1;

    for (let i = 0; i < trucks.length; i++) {
        const truck = trucks[i];

        while (sideLane.length > 0 && sideLane[sideLane.length - 1] === current) {
            sideLane.pop();
            current++;
        }

        if (truck === current) {
            current++;
        } else {
            sideLane.push(truck);
        }
    }

    while (sideLane.length > 0 && sideLane[sideLane.length - 1] === current) {
        sideLane.pop();
        current++;  
    }

    return current === n + 1 ? "yes" : "no";
}

const n = 5;
const trucks = [5, 1, 2, 4, 3];
const res = canSortTrucks(trucks, n);
console.log(res);
