/* ==========================================
    第一种解法：常规解法，不用库，纯数学
 ========================================== */
function getDayOfWeek(timestamp) {
    // 1. 一天的毫秒数
    const ONE_DAY = 24 * 60 * 60 * 1000;

    // 2. 计算经过的天数，并向下取整
    const days = Math.floor(timestamp / ONE_DAY);

    // 3. 映射日期
    const daysLists = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    return daysLists[(days + 1) % 7];

}

getDayOfWeek(1775492249000)

/* ==========================================
    第一种解法：使用Date内置库
 ========================================== */
function getDayOfWeekDate(timestamp){
    // 1. 获取date，单位是毫秒
    const date = new Date(timestamp); // 得到的日期
    console.log(date.getUTCDay());
    const daysList = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

    // 2. 利用getUTCDay()获取
    return daysList[date.getUTCDay()];

}
getDayOfWeekDate(1775492249000)