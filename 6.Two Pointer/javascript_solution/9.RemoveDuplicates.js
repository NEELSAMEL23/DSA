function removeDuplicated(arr,n){
    
    arr.sort()
    
    i = 1
    j = 0
    
    while(i<arr.length){
        
        if(arr[i] !== arr[j]){
            j++
            arr[j] = arr[i]
        }
        i++
    }
    
    return arr.slice(0,j+1)
}


arr = [1,1,2,3,5]
n = 5
res = removeDuplicated(arr,n)
console.log(res.join(" "))

  




// Time Complexity Analysis
// The function removes duplicates from a sorted array using the Two Pointer technique with a while loop.
// The while loop runs once through the array from index 0 to N-1.
// Each element is checked exactly once, and at most, it gets reassigned once.
// There are no nested loops, so the total number of operations is proportional to N.
// Thus, the time complexity is O(N), where N is the length of the array.



// Space Complexity
// The function modifies the array in place (i.e., it doesn't use an extra array).
// Only a few extra variables (i and j) are used.
// Therefore, the space complexity is O(1).