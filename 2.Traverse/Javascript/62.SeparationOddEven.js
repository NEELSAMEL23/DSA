function SeprationOddEven(arr, Q) {

    let odd = []
    let even = []

    for (let num of arr) {
        if (num % 2 == 0) {
            even.push(num)
        } else {
            odd.push(num)
        }
    }

    if (Q === 1) {
        return even.concat(odd)
    } else {
        return odd.concat(even)
    }

}

let arr = [1, 2, 3, 4, 5]
let Q = 1
let res = SeprationOddEven(arr, Q)
console.log(...res)