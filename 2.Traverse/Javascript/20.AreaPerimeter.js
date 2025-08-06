const Area_Perimeter = (L1,B1,L2,B2)=>{
    var Area_Triangle1 = L1 * B1
    var Area_Triangle2 = L2 * B2

    var Area_Perimeter1 = 2*(L1+B1)
    var Area_Perimeter2 = 2*(L2+B2)
    
    if (Area_Triangle1 > Area_Triangle2){
        console.log(true)
    }
    else{
        console.log(false)
    }
    
    if (Area_Perimeter1 > Area_Perimeter2){
        console.log(true)
    }
    else{
        console.log(false)
    }

}

var L1 = 1 
var L2 = 2
var B1 = 2
var B2 = 3

Area_Perimeter(L1,B1,L2,B2)
