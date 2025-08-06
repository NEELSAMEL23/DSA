N = 4

for(let i = 1; i<=N;i++){
    store = 0
    for(let j=1;j<=i;j++){
        if (j%2==0){
            store += j
        }
    }   
    console.log(store)
}
