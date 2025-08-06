const s = "ab#d";
const result = [];

for(let char of s){
    
    if(result.length > 0 && char === '#'){
        result.pop()
    }else{
        result.push(char)
    }
}

console.log(result.join(''))