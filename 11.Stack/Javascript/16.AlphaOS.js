function simplifyPath(path) {
    const parts = path.split('/');
    const stack = [];

    for (const part of parts) {
        if (part === '' || part === '.') {
            continue; // ignore empty and current directory
        } else if (part === '..') {
            if (stack.length > 0) {
                stack.pop(); // go one level up
            }
        } else {
            stack.push(part); // add directory to path
        }
    }

    return '/' + stack.join('/');
}

// Sample Test
const path = "/alpha/../beta/gamma/./delta//.";
console.log(simplifyPath(path));     // Output: "/beta/gamma/delta"
