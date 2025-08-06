function kBeautyOfNumBrute(num, k) {
    const numStr = num.toString();
    let count = 0;

    const start = Math.pow(10, k - 1);
    const end = Math.pow(10, k);

    for (let i = start; i < end; i++) {
        const iStr = i.toString();
        if (numStr.includes(iStr) && num % i === 0) {
            // Count how many times iStr appears in numStr
            let idx = 0;
            
            while ((idx = numStr.indexOf(iStr, idx)) !== -1) {
                count++;
                idx++;  // Move forward to avoid infinite loop
            }
        }
    }

    return count;
}

// Example usage
const num = 430043;
const k = 2;
const res = kBeautyOfNumBrute(num, k);
console.log(res);
