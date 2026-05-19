
function sleptDebt(hoursSlept, targetHours){
    // 1. 变量设定
    // 1.1、过去几天睡觉总和
    const pastTotal = hoursSlept.reduce((acc, cur) => acc + cur, 0);
    console.log(pastTotal);
    // 1.2、过去几天的天数
    const n = hoursSlept.length;
    // 1.3、根据targetHours计算需要睡觉的总小时数，包含今天
    const needTotal = targetHours * (n + 1);

    // 2. 开始判定
    if(pastTotal >= needTotal) {
        return 0;
    }

    return needTotal - pastTotal;
}

console.log(sleptDebt([6, 6, 6, 6, 6, 6], 8));