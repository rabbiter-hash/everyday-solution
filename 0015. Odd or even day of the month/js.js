/* ==========================================
    第一种解法：常规解法，根据题目要求依次写代码
 ========================================== */
function oddOrEvenDay(timestamp){
    // 1. 获取当前时间戳下的具体日期
    const dt = new Date(timestamp);
    console.log(dt);

    // 2. 获取当前日期的日的数值
    const currentTimeStampDay = dt.getUTCDate(); // 请注意是utcDate
    console.log(currentTimeStampDay);

    // 3. 返回
    return (currentTimeStampDay % 2 === 0) ? "even" : "odd";
}

console.log(oddOrEvenDay(1769472000000)); // odd
console.log(oddOrEvenDay(1769444440000)); // even
console.log(oddOrEvenDay(6739456780000)); // odd
console.log(oddOrEvenDay(1)); // odd
console.log(oddOrEvenDay(86400000)); // even