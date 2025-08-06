function traverseArray(arr, N, M){
    let res = []
    
    for(let j=0;j<M;j++){
        
        for(let i=N-1;i>=0;i--){
            res.push(arr[i][j])
        }
    }

    return res.join(' ')
}

let arr = [
    [1, 8, 9],
    [2, 7, 10],
    [3, 6, 11],
    [4, 5, 12]
];

let N = 4;
let M = 3;

let res = traverseArray(arr, N, M);
console.log(res);  // Output: 4 3 2 1 5 6 7 8 12 11 10 9