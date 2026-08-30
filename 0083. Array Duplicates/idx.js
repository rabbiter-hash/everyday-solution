function findDuplicates(arr) {
    // 使用暴力枚舉法進行
    // 1. 初始化存儲結果
    let results = [];

    // 2. 开始循环，循环的目的是对相邻两个元素进行比较
    for(let i = 0; i < arr.length; i++){
        // 3. 内层循环出下一个元素
        for(let j = i + 1; j < arr.length; j++){
            // 判定当前循环中内外层元素是否相等
            if(arr[i] === arr[j]){
                // 检查结果数组中是否已经存在
                let alreadyExists = false;
                for(k = 0; k < results.length; k++){
                    // 如果results中有元素等于当前循环的元素，就退出循环
                    if(results[k] === arr[i]) {
                        // 说明已经存在
                        alreadyExits = true;
                        // 退出当前循环
                        break;
                    }
                }
                // 检查alreadyExists变量
                if(!alreadyExists) {
                    // 如果相等又不存在于结果数组，就加入
                    results.push(arr[i]);
                }

                // 加入还有直接退出循环
                break;
            }
        }
    }
    // 查看一下结果

    console.log(results.sort((a, b) => a - b));
    return results.sort((a, b) => a - b);
}
findDuplicates([1, 2, 3, 4, 1, 2])

function findDuplicatesSorted(arr) {
    // 利用排序进行相邻元素判断
    // 1. 先对原数组进行排序
    let sorted = arr.sort((a, b) => a - b);
    console.log(sorted);
    // 2. 初始化结果集
    let results = [];

    // 3. 开始循环；
    for(let i = 0; i < sorted.length; i++){
        // 比较相邻元素
        if(sorted[i] === sorted[i+1]){
            // 避免重复添加，检查是否在结果数组中
            if(results.length === 0 || results[results.length - 1] !== sorted[i]){
                results.push(arr[i]);
            }
        }
    }
    console.log(results);
    return results;
}
findDuplicatesSorted([1, 2, 3, 4, 1, 2])

function findDuplicatesHash(arr){
    // 利用哈希表记录值出现的次数
    // 1. 初始化哈希表
    let count = {};
    // 2. 初始化结果集
    let results = [];
    // 3. 第一遍遍历，计数
    for (let i = 0; i < arr.length; i++) {
        // 元素
        let num = arr[i];
        if (count[num] === undefined) {
            count[num] = 1; // 第一次出现
        } else {
            count[num]++; // 多次出现就+1
        }
    }

    // 4. 第二次遍历，找出哈希表中统计>=2的值
    for (let key in count) {
        // 打印一下元素看
        console.log(key);
        if(count[key] >= 2) {
            // 查看当前key的值的统计是否大于2，如果大于，就加入到结果集中
            console.log(typeof key);
            results.push(Number(key)); // 转为数字
        }
    }
    console.log(results);
    return results.sort((a, b) => a - b);
}

findDuplicatesHash([1, 2, 3, 4, 1, 2])