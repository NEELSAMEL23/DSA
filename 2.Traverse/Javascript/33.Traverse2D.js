function traverseArray(arr, N, M){
    let res = []
    
    for(let j=M-1;j>=0;j--){
        
        for(let i=0;i<N;i++){
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
console.log(res);  // Output: 9 10 11 12 8 7 6 5 1 2 3 4