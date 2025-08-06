function threeSum(nums) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const result = new Set();

    for (let i = 0; i < n - 2; i++) {
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let left = i + 1;
        let right = n - 1;

        while (left < right) {
            const total = nums[i] + nums[left] + nums[right];

            if (total === 0) {
                const triplet = [nums[i], nums[left], nums[right]];
                result.add(triplet.toString()); // Store as comma-separated string
                left++;
                right--;
            } else if (total < 0) {
                left++;
            } else {
                right--;
            }
        }
    }

    // Convert set of strings back to sorted list of triplets
    const uniqueTriplets = Array.from(result).map(str =>
        str.split(',').map(Number)
    );

   

    // Output the result
    console.log(uniqueTriplets.length);
    for (const triplet of uniqueTriplets) {
        console.log(...triplet);
    }
}

// 🔸 Hardcoded input
const nums = [0, 1, 2, -1, -4, -1];

// 🔸 Function call
threeSum(nums);
