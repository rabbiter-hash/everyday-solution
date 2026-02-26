/* ==========================================
    第一种解法：for 循环
 ========================================== */

function findDifferences(arr){
    if(!isArray(arr) || arr.length === 0){
        throw new TypeError("必须是数组且长度大于1！");
    }
    // 1. 结果集
    let result = [];
    // 2. 循环
    for(let i = 0; i < arr.length - 1; i++){
        result.push(arr[i+1] - arr[i]);
    }
    // 3. 最后一个补0
    result.push(0);

    return result;
}

/* ==========================================
    第二种解法：使用map函数
 ========================================== */
function findDifferencesWithMap(arr){
    // 1. 判定是否为数组并且长度
    if(!Array.isArray(arr) || arr.length === 0){
        throw new TypeError("必须是数组且长度大于0！");
    }
    // 2. 使用map
    return arr.map((num, i) =>
        i === arr.length - 1 ? 0 : arr[i + 1] - num
    );
}
console.log(findDifferencesWithMap([1, 2, 4, 7]))

/* ==========================================
    第三种解法：使用slice + map
 ========================================== */
function findDifferenceWithSliceAndMap(arr){
    // 1. 判定是否为数组
    if(!Array.isArray(arr) || arr.length === 0) {
        throw new TypeError("必须是数组且长度大于0！");
    }
    // 2. 使用slice（切片）+ map
    return arr
        .slice(0, -1)
        .map((num, i) => arr[i + 1] - num)
        .concat(0);
}

/* ==========================================
    第三种解法：使用reduce
 ========================================== */
function findDifferenceWithReduce(arr){
    // 1. 判定数值
    if(!Array.isArray(arr) || arr.length === 0){
        throw new TypeError("必须是数组且长度大于1");
    }
    // 2. 使用reduce
    return arr.reduce((acc, cur, i) => {
        if(i < arr.length - 1){
            acc.push(arr[i + 1] - cur);
        } else {
            acc.push(0);
        }
        return acc;
    }, [])
}

console.log(findDifferenceWithReduce([1, 2, 4, 7]));