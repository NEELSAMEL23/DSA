function secondMaximum(a, b, c) {
    if ((a > b && a < c) || (a > c && a < b)) {
        console.log(a)
    } else if ((b > a && b < c) || (b > c && b < a)) {
        console.log(b)
    } else {
         console.log(c);
    }
}

var a = 3
var b = 7
var c = 5

let res = secondMaximum(a, b, c)
console.log(res)