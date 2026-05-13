function getFrequency(s){
    // 1. 结果集
    let freq = {};

    // 2. 遍历
    for(let char of s){
        freq[char] = (freq[char] || 0) + 1;
    }

    return freq;
}


function getFrequencyWithMap(s){
    // 1. 结果存储对象
    const result = {};
    // 2. 展开字符串
    const chars = [...s];

    // 3. 遍历
    for(let char of chars){
        result[char] = chars.filter(c => c === char).length;
    }
    console.log(result);
}

getFrequencyWithMap("hello")