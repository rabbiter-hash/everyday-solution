/* ==========================================
    第一种解法：常规遍历法
 ========================================== */
function largestNumber(str){
    // 1、判定输入是否合法
    if(!typeof str === "string"){
        throw new TypeError("Input must be a string!");
    }

    // 2. 初始化
    let nums = [];
    let current = "";

    // 3. 开始循环
    for(const ch of str){
        // 判定是否为数字和是否为小数点
        // console.log(typeof ch); // string
        if(/\d/.test(ch) || ch === "."){
            // console.log(ch);
            current += ch;
            // console.log(current);
        } else if(ch === "-" && current === ""){
            current = "-";
        } else {
            if(current && current !== "-"){
                nums.push(current);
            }
            current = "";
        }
    }
    // 4. 处理最后一个值
    if(current){
        nums.push(current);
    }
    // console.log(nums);

    // 5. 求取最大值
    const largest = nums.reduce((max, cur) => {
        return parseFloat(cur) > max ? parseFloat(cur) : max;
    }, -Infinity);

    return largest % 1 === 1 ? parseInt(largest) : parseFloat(largest);
}
console.log(largestNumber("4;15:60,26?52!0"));

/* ==========================================
    第二种解法：使用正则
 ========================================== */
function largestNumberRegx(str){
    // pattern
    const matches = str.match(/-?\d+(\.\d+)?/g);
    if(!matches) {
        return null;
    }

    const largest = matches.reduce((max, val) => {
        return parseFloat(val) > max ? parseFloat(val) : max;
    }, -Infinity);

    // 返回整数还是浮点数
    return matches.includes(largest.toString()) && largest % 1 === 0 ? parseInt(largest) : largest;
}

console.log(largestNumberRegx("4;15:60,26?52!0"));
