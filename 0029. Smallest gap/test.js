/* ==========================================
    第一种解法：暴力遍历
 ========================================== */
function smallestGap(str) {
    // 1. 判定数据输入的合法性
    if(typeof str !== "string") {
        throw new Error("输入必须是字符串！");
    }

    // 2. 初始化最小gap和结果
    let minGap = Infinity;
    let result = "";

    // 3. 暴力循环
    for (let i = 0; i < str.length; i++) {
        for (let j = i + 1; j < str.length; j++){
            if(str[i] === str[j]){
                // 计算最小gap
                let gap = j - i - 1;
                // 判定gap是否小于minGap，小于就将更新minGap
                if(gap < minGap){
                    minGap = gap;
                    // 计算结果
                    result = str.slice(i + 1, j);
                }
            }
        }
    }
    console.log(result);
    return result;
}

// smallestGap("ABCDAC");

/* ==========================================
    第二种解法：哈希表解法
 ========================================== */
function smallestGapWithHashTable(str){
    // 1. 判定数据输入是否合法
    if(typeof str !== "string"){
        throw new Error("输入必须是字符串！");
    }

    // 2. 初始化哈希表、最小gap和结果
    let lastPos = {};
    let minGap = Infinity;
    let result = "";

    // 3. 开始循环
    for(let i = 0; i < str.length; i++){
        // 初始化char
        let char = str[i];
        // 判定char是否在哈希表中
        if(char in lastPos){
            // 如果在，我们就要计算最小gap
            let gap = i - lastPos[char] - 1; // 当前索引-在哈希表中的记录的索引值 - 1
            // 打印调试信息看
            console.log({
                  i,
                  char,
                  lastPos,
                  gap,
                  minGap,
                  result
                });

            // 判定是否小于最小gap
            if(gap < minGap){
                // 更新minGap
                minGap = gap;
                // 拿到最小gap后，就可以取出结果了
                result = str.slice(lastPos[char] + 1, i); //
            }
        }
        // 更新哈希表
        lastPos[char] = i;
    }
    console.log(result);
    return result;
}
smallestGapWithHashTable("ABCDAC");
