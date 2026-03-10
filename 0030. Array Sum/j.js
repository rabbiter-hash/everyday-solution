/* ==========================================
    第一种解法：遍历相加
 ========================================== */
function sumArray(numbers){
    // 1. 判定数据是否合法
    if(!Array.isArray(numbers)){
        throw new Error("输入必须是数组！");
    }

    // 2. 初始化计数器
    let total = 0;

    // 3. 遍历相加
    for(let i=0; i<numbers.length; i++){
        if(typeof numbers[i] !== "number"){
            // 跳过当前循环
            continue;
        }
        total += numbers[i];
    }
    console.log(total);
    return total;
}
sumArray([1, 2, 3, 4, 5]);

function sumArrayWithForOf(numbers) {
    // 简化上方解法
    // 1. 判定是否符合要求
    if(!Array.isArray(numbers)){
        throw new Error("输入必须是数字！");
    }

    // 2. 初始化计数器
    let total = 0;

    // 3. 用for of循环
    for(const num of numbers){
        if(typeof num === "number"){
            // console.log(num);
            total += num;
        }
    }
    console.log(total);
    return total;
}
sumArrayWithForOf([1, 2, 3, 4, 5]);

/* ==========================================
    第二种解法：使用reduce函数
 ========================================== */
function sumArrayWithReduce(numbers){
    // 1. 判定输入是否合法
    if(!Array.isArray(numbers)){
        throw new Error("输入必须是数组！");
    }

    // 2. 累加器
    return numbers.reduce((acc, cur, i, oarr) => {
        return typeof cur === "number" ? acc + cur : acc;
    }, 0)
}

console.log(sumArrayWithReduce([1, 2, 3, 4, 5, 6])); // 21