function reverseWords(sentence) {
    const words = sentence.split(" ");
    const reversedWords = words.map(word => word.split('').reverse().join(''));
    return reversedWords.join(" ");
}

let n = 11;
let sentence = "hello world";
let res = reverseWords(sentence);
console.log(res);
