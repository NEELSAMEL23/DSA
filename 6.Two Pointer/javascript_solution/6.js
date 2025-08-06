function countCommonElements(arr1, arr2){
    arr1.sort()
    arr2.sort()

    i = 0
    j = 0
    count = 0
    
    while(i<arr1.length-1 && j<arr2.length-1){
        
        if(arr1[i]===arr2[j]){
            count++
            i++
            j++
        }else if(arr1[i] < arr2[j]){
            i++
        }else{
            j++
        }    
    }
    return count
}

let arr1 = [1,2,2,3,4,5] 
let arr2 = [4,4,3,2,1,1]
let res = countCommonElements(arr1, arr2)
console.log(res)


 


// The time complexity of the countCommonElements function can be broken down into the following steps:
// Sorting the arrays:
// The sort() function has a time complexity of O(n log n), where n is the length of the array.
// Sorting both arrays A and B takes O(n log n) for A and O(m log m) for B, where n and m are the lengths of arrays A and B respectively.
// Traversing both arrays:
// The while loop runs as long as both i < len(A) and j < len(B).
// In the worst case, it can loop for a number of steps equal to the sum of the lengths of both arrays: O(n + m).

// Overall Time Complexity:
// Sorting both arrays: O(n log n + m log m)
// Traversing both arrays: O(n + m)
// Thus, the overall time complexity is:
// O(n log n + m log m)

// Where:
// n is the length of array A
// m is the length of array B
// In the case where both arrays are of the same length, this simplifies to O(n log n).



// Total Space Complexity:
// O(1) for auxiliary space (constant space for the variables).

// The space used by the input arrays A and B does not count toward additional space complexity because they are 
// provided as input and not created or duplicated.






