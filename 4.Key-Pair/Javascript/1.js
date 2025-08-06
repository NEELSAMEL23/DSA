function pairMatch(pairs) {
    const pairMap = {
        ')': '(',
        '}': '{',
        ']': '['
    };
    const stack = [];

    for (let char of pairs) {
        if (Object.values(pairMap).includes(char)) {
            stack.push(char);
        } else if (pairMap.hasOwnProperty(char)) {
            if (!stack.length || pairMap[char] !== stack.pop()) {
                return false;
            }
        }
    }
    return stack.length === 0;
}

const pairs = "{[()]}";
const res = pairMatch(pairs);
console.log(res); // Output: true
