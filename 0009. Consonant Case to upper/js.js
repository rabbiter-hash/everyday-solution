
function consonantCase(str){
    // 1. 判断是否是str，如果不是，直接返回
    if(typeof str !== "string") {
        return "不是字符串，拜拜！";
    }

    // 2. 元音字母集合
    let vowels = new Set(['a', 'e', 'i', 'o', 'u']);

    // 3. 结果数组
    let result = [];

    // 4. 循环和判定
    for (const char of str) {
        if(char==="-"){
            // 如果是中划线，就直接在数组中转换成下划线
            result.push("_");
        } else if(vowels.has(char.toLowerCase())){
            // 如果当前字母的小写存在于元音字母集合中，就追加当前字母的小写到数组
            result.push(char.toLowerCase());
        } else if(/[a-zA-Z]/.test(char)){
            // 正则匹配是否是字母
            result.push(char.toUpperCase());
        } else {
            result.push(char);
        }
    }
    return result.join("");
}
console.log(consonantCase("-heloeee-"))
