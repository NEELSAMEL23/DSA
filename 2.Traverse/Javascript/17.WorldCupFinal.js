function worldCupFinal(NzScore, NzSuperOver, NzFours, EngScore, EngSuperOver, EngFours) {
    if (NzScore > EngScore) {
        console.log("New Zealand");
    } else if (NzScore < EngScore) {
        console.log("England");
    } else if (NzSuperOver > EngSuperOver) {
        console.log("New Zealand");
    } else if (NzSuperOver < EngSuperOver) {
        console.log("England");
    } else if (NzFours > EngFours) {
        console.log("New Zealand");
    } else if (NzFours < EngFours) {
        console.log("England");
    }
}

var NzScore = 241
var NzSuperOver =  15
var NzFours = 21

var EngScore = 241
var EngSuperOver = 15  
var EngFours = 26

worldCupFinal(NzScore, NzSuperOver, NzFours, EngScore, EngSuperOver, EngFours)