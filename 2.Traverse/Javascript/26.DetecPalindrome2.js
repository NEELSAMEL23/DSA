function palindrome(num){
    let str = num.toString()

    let rever_str = str.split("").reverse().join("")

    if(str==rever_str){
        return true
    }else{
        return false
    }
}

num = 123
res = palindrome(num)
console.log(res)

