/*
    解法一：使用硬编码映射
 */
function getWordScore(word){
    // 1. 映射值
    const letterValues = {
          A: 1,
          B: 2,
          C: 3,
          D: 4,
          E: 5,
          F: 6,
          G: 7,
          H: 8,
          I: 9,
          J: 10,
          K: 11,
          L: 12,
          M: 13,
          N: 14,
          O: 15,
          P: 16,
          Q: 17,
          R: 18,
          S: 19,
          T: 20,
          U: 21,
          V: 22,
          W: 23,
          X: 24,
          Y: 25,
          Z: 26
        };

    // 2. 初始化累加值
    let total = 0;

    // 3. 循环
    for(let ch of word){
        ch = ch.toUpperCase();
        total += letterValues[ch];
    }
    return total;
}
getWordScore("hi");

/*
    解法二：使用函数
 */
function getWordScoreUseCharCodeAt(word){
    // 1. 初始化累加值
    let total = 0;

    // 2. 循环
    for (let ch of word.toUpperCase()){
        // 只处理A-Z
        if(ch >= "A" && ch <= "Z"){
            total += ch.charCodeAt(0) - 64;
        }
    }
    return total;

}

/*
    解法三：Idiomatic
 */
function getWordScoreIdiomatic(word){
    return [...word.toUpperCase()]
        .filter(ch => ch >= "A" && ch <= "Z")
        .reduce((acc, ch) => acc + ch.charCodeAt(0) - 64, 0);
}