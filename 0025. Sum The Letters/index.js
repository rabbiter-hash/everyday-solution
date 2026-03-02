/* ==========================================
    第一种解法：for 循环
 ========================================== */
function sumLettersWithFor(str){
    // 1. 判定数据是否和发
    if(typeof str !== "string") {
        throw new Error("输入必须是非空字符串！");
    }

    // 2. 累加器
    let total = 0;

    // 3. 循环
    for(let i = 0; i < str.length; i++){
        let char = str[i];

        // 正则提取字母
        if(/[a-zA-Z]/.test(char)) {
            total += char.toLowerCase().charCodeAt(0) - 96;
            // 97是'a'
        }
    }
    return total;
}

console.log(sumLettersWithFor("abc"));
console.log("a".charCodeAt(0));

/* ==========================================
    第二种解法：用ascii范围判定，更底层
 ========================================== */
function sumLettersWithAscii(str){
    // 1. 累加值
    let total = 0;

    for (let i=0; i < str.length; i++){
        let code = str[i].toLowerCase().charCodeAt(0);

        if(code >= 97 && code <= 122) {
            total += code - 96;
        }
    }
    return total;
}
console.log(sumLettersWithAscii("abc"));

/* ==========================================
    第三种解法：split + reduce
 ========================================== */
function sumLettersWithSplitPlusReduce(str){
    // 1. 判定输入的合法性
    if(typeof str !== "string" || str.length === 0){
        throw new Error("输入必须是非空字符串！");
    }

    // 2. 转小写 -> 分数组 -> 累加
    return str
        .toLowerCase()
        .split("")
        .reduce((acc, cur) => {
            let code = cur.charCodeAt(0);
            if(code >= 97 && code <= 122){
                return acc + (code - 96);
            }
            return acc;
        }, 0)
}
console.log(sumLettersWithSplitPlusReduce("abc"));


/* ==========================================
    第四种解法：match + reduce
 ========================================== */
function sumLettersWithMatchPlusReduce(str){
    // 1. 判定数据合法性
    if(typeof str !== "string" || str.length === 0) {
        throw new Error("输入必须是非空字符串！");
    }

    // 2. 将字母匹配出来
    const letters = str.match(/[a-zA-Z]/g);
    if(!letters) return 0;
    console.log(letters);
    return letters.reduce((acc, cur) => {
        return acc + cur.toLowerCase().charCodeAt(0) - 96;
    }, 0);

}
console.log(sumLettersWithMatchPlusReduce("ab c e"));

/* ==========================================
    第五种解法：极限性能for，不生成数组
 ========================================== */
function sumLettersNormal(str) {
    // 1. 判定输入是否合法
    if(typeof str !== "string" || str.length === 0){
        throw new Error("输入必须是非空字符串！");
    }

    // 2. 累加器
    let total = 0;

    // 3. 循环
    for(let i = 0; i < str.length; i++){
        let code = str.charCodeAt(i);

        // A - Z
        if(code >= 65 && code <= 90) {
            total += code - 64;
        }
        // a - z
        else if(code >= 97 && code <= 122){
            total += code - 96;
        }
    }
    return total;
}

console.log(sumLettersNormal('ab,.1c3'));