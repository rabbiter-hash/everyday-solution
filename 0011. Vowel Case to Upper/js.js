
function vowelCase(str){
    /* 注释 ====================================================
        // 元音字母转大写
           辅音字母转小写
           其他的保持不变
     */
    // 1. 判定是否是string
    if(typeof str !== "string") {
        return "不是字符串，拜拜！";
    }

    // 2. 定义元音集合
    let vowels = new Set(['a', 'e', 'o', 'i', 'u']);

    // 3. 结果数组
    let result = [];

    // 4. 循环
    for (const char of str){
        // 如果有元音，就转大写
        if(vowels.has(char.toLowerCase())){
            result.push(char.toUpperCase());
        } else if(/[a-zA-Z]/.test(ch)){
            // 如果是辅音，就转小写
            result.push(char.toLowerCase());
        } else {
            // 其他直接追加
            result.push(char);
        }
    }
    return result.join('');
}