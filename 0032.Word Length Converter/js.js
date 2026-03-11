
/* ==========================================
    第一种解法：循环遍历
 ========================================== */
function convertWords(str) {
    const words = str.split(" ");   // 拆分单词
    const result = [];              // 存放长度

    for (let i = 0; i < words.length; i++) {
        result.push(String(words[i].length));
    }

    return result.join(" ");        // 拼接字符串
}

/* ==========================================
    第二种解法：map映射
 ========================================== */
function convertWordsWithMap(str) {
    return str
        .split(" ")
        .map(word => String(word.length))
        .join(" ");
}

/* ==========================================
    第三种解法：map映射但是更简洁
 ========================================== */
function convertWordsWithMapSimple(str) {
    return str
        .split(" ")
        .map(wrod => word.length)
        .join(" ");
}
