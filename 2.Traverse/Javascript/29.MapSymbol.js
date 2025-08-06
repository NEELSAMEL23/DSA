function symbol(num){
    let symbol = ["!","@","#","$","%","^","&","*"]

    for(let i=0; i<symbol.length; i++){
        console.log(`${symbol[i]}-${num+i*2}`)
    }
}

var num = 20
res = symbol(num)
console.log(res)