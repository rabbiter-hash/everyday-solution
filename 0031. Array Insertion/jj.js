/* ==========================================
    第一种解法：循环遍历加条件判定
 ========================================== */
function insertIntoArrayWithFor(arr, value, index){
    // 1. 判定数据的合法性
    if(!Array.isArray(arr)){
        throw new Error("第一个参数必须是数组！");
    }

    if(typeof index !== "number"){
        throw new Error("index必须是整数！");
    }

    // 2. 结果集
    let result = [];

    // 3. 开始遍历
    for(let i=0; i<arr.length; i++){
        // js没有enumerate，只能定义变量
        let item = arr[i];
        // 判定i是否跟index相等
        if(i === index){
            result.push(value);
        }
        // 回到正常for流程
        result.push(item);
    }
    return result;
}
console.log(insertIntoArrayWithFor([2, 4, 8, 10], 6, 2));

/* ==========================================
    第二种解法：数组切片
 ========================================== */
function insertIntoArrayWithSlice(arr, value, index){
    // 1. 判定数据的合法性
    if(!Array.isArray(arr)){
        throw new Error("第一个参数必须是数组！");
    }

    if(typeof index !== "number"){
        throw new Error("index必须是整数！");
    }

    // 2. 切片返回，js数组相加用concat
    return arr.slice(0, index).concat([value], arr.slice(index));
}
console.log(insertIntoArrayWithSlice([2, 4, 8, 10], 6, 2));

/* ==========================================
    第三种解法：原地修改数组，js原地修改数组的方法为splice()
 ========================================== */
function insertIntoArrayWithSplice(arr, value, index){
    // 1. 判定数据的合法性
    if(!Array.isArray(arr)){
        throw new Error("第一个参数必须是数组！");
    }

    if(typeof index !== "number"){
        throw new Error("index必须是整数！");
    }

    // 2. 原地修改数组
    arr.splice(index, 0, value); // 在索引为index的地方插入值为value的元素，0表示删除0个元素

    return arr.slice(); // 返回数组的副本
    // 其实也可以先复制数组，然后用新数组去splice
}
console.log(insertIntoArrayWithSplice([2, 4, 8, 10], 6, 2));