N = 5
for(let i=0;i<N;i++){
    res = ""
    for(let j=0;j<N;j++){
        if (i==0 || j==0 || j==N-1){
            res += "* "
        }else{
            res += " "
        }
        
    }
    console.log(res)
}