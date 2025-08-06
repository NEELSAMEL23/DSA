function appear_once(arr,N){
    
    let pair_map = {}
    
    for(let i=0;i<N;i++){
        if(arr[i] in pair_map){
            pair_map[arr[i]] += 1
        }else{
            pair_map[arr[i]] = 1
        }
    }


    let sum = 0
    for(let key in pair_map){

        if(pair_map[key]===1){
           sum += Number(key)
        }
    }
    return sum
}




let arr = [3,5,3,3,8,5,6]
let N = 7
let res = appear_once(arr,N)
console.log(res)