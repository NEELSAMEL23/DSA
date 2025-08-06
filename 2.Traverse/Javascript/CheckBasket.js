let n = 3;
let fruits = ['banana', ' banana', 'banana'];

// Trim spaces and create a Set to get unique fruits
let unique_fruits = new Set(fruits.map(fruit => fruit.trim()));

if (unique_fruits.size === 1) {
    console.log("Single Type");
} else {
    console.log("Mixed Basket");
}
