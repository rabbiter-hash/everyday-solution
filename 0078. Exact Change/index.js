
function exactChange(amount) {
    // 1. 初始化统计值
    let count = 0;

    // 2. 开始暴力枚举
    // 2.1、首先是quarter （25美分）
    for(let q = 0; q <= Math.floor(amount / 25 ); q++) {
        let remainingAfterQ = amount - q * 25;

        // 2.2、其次dimes
        for(let d = 0; d <= Math.floor(remainingAfterQ / 10); d++){
            let remainingAfterD = remainingAfterQ - d * 10;
            // nickel 可以从 0 到 remainingAfterD / 5
            // 剩下的全部用 pennies 补齐
            for (let n = 0; n <= Math.floor(remainingAfterD / 5); n++) {
                count++;
            }
        }
    }
    console.log(count);
    return count;
}

exactChange(9);