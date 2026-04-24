
function compress(str){
    // 1. 将字符串拆分成数组
    const wordsArr = str.split(/\s+/g);

    // 2. 存储结果集
    // 2.1、字符串第一次出现位置的映射
    let wordsIndexMap = {};
    // 2.2、结果集
    let results = [];

    // 3. 循环遍历
    wordsArr.forEach((word, inx) => {
        // 判定word是否在映射表中
        if(!(word in wordsIndexMap)){
            // 不存在就追加
            /*
            * 也可以使用
            * 1. if(wordsIndexMap.hasOwnProperty(word))
            * 2. if(Object.hasOwn(wordsIndexMap, word))
            * */
            wordsIndexMap[word] = inx + 1;
            // 将word追加到结果集
            results.push(word);
        } else {
            // 如果word在哈希表中，就追加哈希表中对应字段的值
            results.push(wordsIndexMap[word]);
        }
    });
    // console.log(results);
    return results.join(" ");
}

compress("the cat sat on the mat on which the cat sat");

function compressIdiomatic(str){
    const seen = new Map();

    return str
        .split(/\s+/g)
        .map((word, i) => {
            if(seen.has(word)) return seen.get(word);
            seen.set(word, i + 1);
            return word;
        }).join(" ");
}