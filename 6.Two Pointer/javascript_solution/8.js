
function deliveryParcel(parcels, N, K) {
    parcels.sort()
    let i = 0;
    let j = N - 1;
    let vans = 0;

    while (i < j) {
        if (parcels[i] + parcels[j] <= K) {
            i++;
        } 
        j--;
        vans++;
    }
    return vans;
}

const N = 4;
const K = 3;
const parcels = [1, 2, 2, 3];
const res = deliveryParcel(parcels, N, K);
console.log(res);

//The time complexity of the deliveryParcel function is O(N)