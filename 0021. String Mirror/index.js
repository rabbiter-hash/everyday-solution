/* ==========================================
    第一种解法：字符串->数组->字符串
 ========================================== */
function mirror(str) {
    // 1. 字符窜 -> 数组
    let arr = [];
    for(let i=0; i<str.length; i++){
        // console.log(i + "======>" + str[i]); // 主要查看边界
        arr.push(str[i]);
    }
    console.log(arr);

    // 2. 拷贝一份数组
    let reversedArr = arr.slice();
    console.log("没有反转之前： ", reversedArr);
    console.log("是否是同一个数组：", arr === reversedArr);

    // 3. 原地反转
    reversedArr.reverse();
    console.log("反转后的数组：", reversedArr);

    // 4. 拼接反转后的数组到原数组arr
    arr.push(...reversedArr);
    console.log("拼接后的数组：",arr); // 等价于python的extend

    // 5. 拼接字符串
    return arr.join("");
}

// mirror("freeCodeCamp");

/* ==========================================
    第二种解法：简化方法1
 ========================================== */
function simpleMirror(str){
    // 1. 转成数组
    let arr = str.split("");
    console.log(arr);
    // 2. 反转数组
    let reversedArr = arr.slice().reverse();
    console.log(reversedArr);

    // 3. 查看数据
    console.log(arr === reversedArr);

    // 4. 拼接数组
    arr.push(...reversedArr);

    // 5. 返回
    return arr.join("");
}
simpleMirror("freeCodeCamp");

/* ==========================================
    第三种解法：split + reverse一句话版
 ========================================== */
function mirrorSplitReverse(str) {
    return str + str.split("").reverse().join("");
}

/* ==========================================
    第四种解法： 完全不可变，不改变任何中间数组
 ========================================== */
function mirrorStand(str) {
    // 1. 用const定义数组
    const arr = str.split("");
    console.log(arr);
    // 2. 反转数组也用const
    const reversedArr = [...arr].reverse();
    console.log(reversedArr);

    // 3. 拼接
    return [...arr, ...reversedArr].join("");
}

/* ==========================================
    第五种解法： 使用reduce
 ========================================== */
function mirrorReduce(str){
    // 使用reduce，每次都将字母往前塞
    return str + str.split("").reduce((acc, ch) => ch + acc, "");
}