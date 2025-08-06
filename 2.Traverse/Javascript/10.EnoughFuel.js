function fuel_consumption(fuel,distance){
    required = fuel * distance
    if (required > 50){
        return "Go On"
    }else{
        return "Enough"
    }
}

var fuel = 1
var distance = 48
var res = fuel_consumption(fuel,distance)
console.log(res)