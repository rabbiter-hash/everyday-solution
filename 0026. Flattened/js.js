
/* ==========================================
    第一种解法：for 循环
 ========================================== */
function isFlat(arr){
    // 1. 判定数据输入
    if(!Array.isArray(arr)) {
        throw new Error("输入必须是数组！");
    }

    // 2. 循环
    for(let i = 0; i < arr.length; i++){
        if(Array.isArray(arr[i])){
            return false;
        }
    }
    return true;
}

/* ==========================================
    第二种解法：every 函数
 ========================================== */
function isFlatWithEvery(arr){
    // 1. 判定数据输入
    if(!Array.isArray(arr)){
        throw new Error("输入必须是数组！");
    }

    // 2. 利用every返回
    return arr.every( item => !Array.isArray(item));
}
console.log(isFlatWithEvery(['2', true]));

/* ==========================================
    第三种解法：some 函数
 ========================================== */
function isFlatWithSome(arr){
    return !arr.some(item => Array.isArray(item));
    // 等同于
    // return !arr.some(Array.isArray);
}
console.log(isFlatWithSome(['1', '2']))

/* ==========================================
    第四种解法：filter 函数
 ========================================== */
function isFlatWithFilter(arr){
    // arr.fitler(Array.isArray)筛选数组
    return arr.filter(Array.isArray).length === 0;
    // 等价于
    // return arr.filter( item => item.length === 0);
}

/* ==========================================
    第五种解法：reduce 函数
 ========================================== */
function isFlatWithReduce(arr) {
    return arr.reduce( (acc, cur) => {
        return acc && !Array.isArray(cur);
    }, true);
}

