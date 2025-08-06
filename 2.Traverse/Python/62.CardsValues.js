function checkDoubleExists(cards) {
    // Convert the array of cards to a Set for faster lookup
    let cardSet = new Set(cards);

    for (let card of cards) {
        // Check if the card has a double in the set (2 * card)
        if (card !== 0 && cardSet.has(2 * card)) {
            return "Yes";
        }
    }

    // If no such pair is found, return "No"
    return "No";
}

N = 4
cards = [1,2,3,4]
res = checkDoubleExists(cards)
console.log(res)