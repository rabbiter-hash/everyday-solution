
function getOddWords(s){
    // 1. 拆分成数组
    let wordsArr = s.split(/\s+/);

    console.log(wordsArr);

    // 2. 结果集
    let results = [];

    // 3. 循环遍历数组
    for(let word of wordsArr){
        if(word.length % 2 !== 0){
            results.push(word);
        }
    }
    console.log(results);
    return results.join(" ");
}

getOddWords("This is a super good test")

function getOddWordsOne(s){
    return s
        .split(/\s+/g)
        .filter(word => word.length % 2 !== 0)
        .join(" ");
}