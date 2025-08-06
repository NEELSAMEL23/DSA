function profile_pic(L,Length,W,Width){
    if( L > Length){
        console.log("Upload")
    }else{
        console.log("Increase Length")
    }

    if( W > Width){
        console.log("Upload")
    }else{
        console.log("Increase Width")
    }
}

L = 12
Length = 8 
W = 14
Width = 19 
profile_pic(L,Length,W,Width)