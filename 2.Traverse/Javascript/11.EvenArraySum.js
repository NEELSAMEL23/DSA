function Even_Array_Sum(arr,N){
    
    let sum = 0
    
    for(let i=0;i<N;i++){
        if(arr[i] % 2==0){
            sum += arr[i]
        }
    }
    
    return sum
}




let N = 5
let arr = [1,2,3,4,5]
let res = Even_Array_Sum(arr,N)
console.log(res)