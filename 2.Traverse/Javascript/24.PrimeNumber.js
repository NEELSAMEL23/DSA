function is_prime(num) {
    if (num <= 1) {
        return false;
    }
    for (let i = 2; i <= Math.floor(Math.sqrt(num)); i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}

let num = 5;
let res = is_prime(num);

if (res) {
    console.log("Yes");
} else {
    console.log("No");
}
