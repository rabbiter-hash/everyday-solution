function getLongestSubstring(str) {
    let longest = "";
    const countMap = new Map();

    // 统计所有子串出现次数
    for (let i = 0; i < str.length; i++) {
        for (let j = i + 1; j <= str.length; j++) {
            let sub = str.slice(i, j);
            countMap.set(sub, (countMap.get(sub) || 0) + 1);
        }
    }

    // 找出现次数大于 1 的最长子串
    for (let [sub, count] of countMap) {
        if (count > 1 && sub.length > longest.length) {
            longest = sub;
        }
    }

    return longest;
}

// getLongestSubstring("abracadabra");
let str = "abracadabra";
let sub = "abra";
console.log(str.split(sub)); // [ '', 'cad', '' ]
console.log(str.split(sub).length - 1); // 2

let a = "aaa";
let suba = "a";
console.log(a.split(suba)); // [ '', '', '', '' ]
console.log(a.length); // 3
console.log(a.split(suba).length); // 4
