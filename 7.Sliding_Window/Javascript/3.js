function  minExpenses(arr, n, k){
    minExp = Infinity
    for(let i=0;i<n-k+1;i++){
        
        sum = 0
        
        for(j=i;j<=i+k-1;j++){
            sum+=arr[j]    
        }
        
        minExp = Math.min(minExp,sum)
    }
    
    return minExp
    
}

const arr = [9, 9, -5, 9, 5];
const n = 5;
const k = 3;

const res = minExpenses(arr, n, k);
console.log(res); // Output: 13