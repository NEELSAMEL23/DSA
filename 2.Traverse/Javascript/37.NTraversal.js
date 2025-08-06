function  traverseArr(arr, N, M){
    let res= []
    
    for(let i=N-1;i>=0;i--){
        res.push(arr[i][0])
    }
    
    for(let i=N-2;i>0;i--){
        res.push(arr[i][i])
    }
    
     for(let i=N-2;i>=0;i--){
        res.push(arr[i][M-1])
    }
    
    return res
}

// Hardcoded input
let arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
let N = 3;
let M = 3;

let res = traverseArr(arr, N, M);
console.log(...res);  // Output: 7 4 1 5 6 3