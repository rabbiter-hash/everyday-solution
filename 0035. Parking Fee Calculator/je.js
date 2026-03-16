/* ==========================================
    第一种解法：常规清晰写法
 ========================================== */
function calculateParkingFee(parkTime, pickupTime){
    // 1. 转换为分钟
    const [eh, em] = entry.split(":").map(Number);
    const [xh, xm] = exit.split(":").map(Number);

    const entryMinutes = eh * 60 + em;
    const exitMinutes = xh * 60 + xm;

    // 2. 判断是否过夜
    let overnight = false;
    let duration;

    if (exitMinutes < entryMinutes) {
        overnight = true;
        duration = (24 * 60 - entryMinutes) + exitMinutes;
    } else {
        duration = exitMinutes - entryMinutes;
    }

    // 3. 向上取整计算小时
    const hours = Math.ceil(duration / 60);

    // 4. 计算费用
    let cost = hours * 3;

    // 5. 过夜费用
    if (overnight) {
        cost += 10;
    }

    // 6. 最低收费
    cost = Math.max(cost, 5);

    return `$${cost}`;
}