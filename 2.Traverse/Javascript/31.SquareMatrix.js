function traverseArray(arr, N, M){
    let res = []
    
    for(let i=0;i<N;i++){
        let arr2 = []
        for(let j=0;j<M;j++){
             arr2.push(arr[i][j] + 1)
        }
        res.push(arr2)
    }
    
    return res.join('\n')
}

let arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

let N = 3;
let M = 3;

let res = traverseArray(arr, N, M);
console.log(res);  
// Output: 
// 2,3,4
// 5,6,7
// 8,9,10