

N = 7
string = "pingpin"

pair_map = {}

for(let i=0;i<N;i++){

    if (string[i] in pair_map){
        pair_map[string[i]] += 1   
    }else{
        pair_map[string[i]] = 1
    }
}

let ping_count = Math.min(pair_map["p"],pair_map["i"],pair_map["n"],pair_map["g"])
console.log(ping_count)