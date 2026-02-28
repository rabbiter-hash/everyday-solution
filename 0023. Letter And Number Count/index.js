/* ==========================================
    第一种解法：单次遍历 + charCode
    只遍历一次
    不生成额外数组
    精准控制 ASCII 范围
    避免 Unicode 字母问题
    时间复杂度：O(n)
    空间复杂度：O(1)
 ========================================== */
function countLettersAndNumbers(str){
    // 1. 首先判定是否为字符串
    if(typeof str !== "string" || str.length === 0){
        throw new Error("Input must-be non-empty string!");
    }

    // 2. 计量统计
    let letterCount = 0;
    let numberCount = 0;

    // 3. 循环
    for(let i = 0; i < str.length; i++){
        const code = str.charCodeAt(i);
        // A-Z
        if(code >= 65 && code <= 90){
            letterCount++;
        }
        // a-z
        else if(code >= 97 && code <= 127){
            letterCount++;
        }
        // 0-9
        else if(code >= 48 && code <= 57){
            numberCount++;
        }
    }
    // 4. 定义字母大小写
    const letterWord = letterCount === 1 ? "letter" : "letters";
    const numberWord = numberCount === 1 ? "number" : "numbers";

    return `The string has ${letterCount} ${letterWord} and ${numberCount} ${numberWord}.`;
}

// console.log(countLettersAndNumbers("helloworld123"));
/* ==========================================
    第二种解法：使用正则
 ========================================== */
function countLettersAndNumbersWithRepr(str){
    if(typeof str !== "string" || str.length === 0){
        throw new Error("Input must-be a non-empty string!");
    }

    // 2. 正则
    const letters = str.match(/[A-Za-z]/g) || [];
    const numbers = str.match(/[0-9]/g) || [];

    const letterCounts = letters.length;
    const numberCounts = numbers.length;

    return `The string has 
            ${letterCounts} ${letterCounts === 1 ? "letter" : "letters"} 
            and 
            ${numberCounts} ${numberCounts === 1 ? "number" : "numbers"}.`;
}
// console.log(countLettersAndNumbersWithRepr("123hellowo"));

/* ==========================================
    第三种解法：filter()函数
 ========================================== */
function countLettersAndNumbersWithFilter(str){
    // 1. 判定
    if(typeof str !== "string" || str.length === 0){
        throw new Error("输入必须是非空字符串！");
    }

    // 2. 解构赋值
    const chars = [...str];

    // 3. 利用filter计算字母
    const letterCounts = chars.filter(
        c =>
            (c >= "A" && c <= "Z") ||
            (c >="a" && c <= "z")).length;

    // 4. 利用filter计算数字
    const numberCounts = chars.filter(d => d >= "0" && d <= "9").length;
    return `The string has ${letterCounts} ${letterCounts === 1 ? "letter" : "letters"} and ${numberCounts} ${numberCounts === 1 ? "number" : "numbers"}.`;
}
// console.log(countLettersAndNumbersWithFilter('hellow1233'));

/* ==========================================
    第四种解法：reduce()函数
 ========================================== */
function countLettersAndNumbersWithReduce(str){
    // 1. 判定
    if(typeof str !== "string" || str.length === 0){
        throw new Error("输入必须是非空字符窜！");
    }

    // 2. 解构
    const result = [...str].reduce((acc, cur) => {
        if((cur >= "A" && cur <= "Z") || (cur >= "a" && cur <= "z")){
            acc.letters++;
        } else if (cur >= "0" && cur <= "9"){
            acc.numbers++;
        }
        return acc;
    }, { letters:0, numbers: 0 })
    return `The string has ${result.letters} ${result.letters === 1 ? "letter" : "letters"} and ${result.numbers} ${result.numbers === 1 ? "number" : "numbers"}.`;
}
console.log(countLettersAndNumbersWithReduce("123hellowa1"));