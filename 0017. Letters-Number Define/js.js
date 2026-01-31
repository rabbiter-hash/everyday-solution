/* 注释 #=============================================
            *** 第一种解法：字符串 +
      ============================================= # */
function separateLettersAndNumbers(str){
    if(!str) throw new TypeError("输入必须是字符串！");

    // 1. 结果集 —— string
    let result = str[0];

    // 2. 遍历，从第二个元素开始，
    for (let i=1; i<str.length; i++){
        // 取出前一个元素和当前元素进行对比
        const prev = str[i-1];
        const curr = str[i];

        // 判定前一个元素和当前元素是否为字母
        const prev_is_letter = /[a-zA-Z]/.test(prev);
        const curr_is_letter = /[a-zA-Z]/.test(curr);

        // 判定是否为同一种元素
        if(prev_is_letter !== curr_is_letter){
            result += "-";
        }
        result += curr;
    }
    return result;
}

console.log(separateLettersAndNumbers("a1b2c3d4"));

/* 注释 #=============================================
            *** 第二种解法：数组 +
      ============================================= # */
function separateLettersAndNumbersWithArray(str) {
    // 1. 简单判定
    if(!str) throw new TypeError("请合法输入！");

    // 2. 结果集 —— 数组
    let result = [str[0]]; // 存入首字母方便比较

    // 3. 从第二个字符开始遍历
    for(let i = 1; i < str.length; i++ ){
        // 取出前一个字符和当前字符
        const prev = str[i-1];
        const curr = str[i];

        // 字母
        const prev_is_letter = /[a-zA-Z]/.test(prev);
        const curr_is_letter = /[a-zA-Z]/.test(curr);

        // 判定
        if(prev_is_letter !== curr_is_letter){
            // 说明前一个元素和当前元素不相同类型
            result.push("-");
        }

        // 正常逻辑流，
        result.push(curr);
    }
    // 4. 返回结果字符串
    return result.join("");
}

console.log(separateLettersAndNumbersWithArray("a1b2c3d4"));


/* 注释 #=============================================
            *** 第三种解法：相邻比较 + isNaN
      ============================================= # */
function separateLettersAndNumbersWithIsNaN(str){
    if(!str) throw new TypeError("请输入正确的字符串！");

    // 2. 结果集
    let res = [str[0]];

    // 3. 遍历
    for(let i = 1; i < str.length; i++){
        // 判定
        if(isNaN(str[i-1]) !== isNaN(str[i])){
            res.push("-");
        }
        res.push(str[i]);
    }
    return res.join("");
}

/* 注释 #=============================================
            *** 第四种解法：reduce
      ============================================= # */
function separateLettersAndNumbersWithReduce(str){
    if(!str) throw new TypeError("请输入有效的字符窜！");

    return [...str].reduce((acc, cur) => {
        // 注意这里的at，acc.at(-1) 相当于 acc[acc.length-1]
        if(acc && (isNaN(acc.at(-1))) !== isNaN(cur)){
            acc += "-";
        }
        return acc + cur;
    }, '');
}