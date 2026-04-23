function getCleanupScore(items) {
    // 1. 分值表
    const values = {
        bottle: 10,
        can: 6,
        bag: 8,
        tire: 35,
        straw: 4,
        cardboard: 3,
        newspaper: 3,
        shoe: 12,
        electronics: 25,
        battery: 18,
        mattress: 38
    };

    // 2. 初始化
    let total = 0;
    let prevItem = null;
    let streak = 0;

    // 3. 遍历
    for(let i = 0; i < items.length; i++){
        let item = items[i];
        let score;
        // console.log(item);

        // =====================
        // Step 1：判断 rare
        // =====================
        if (Array.isArray(item) && item[0] === "rare") {
            score = item[1];

            // 打断 streak
            prevItem = null;
            streak = 0;
        } else {
            // =====================
            // Step 2：基础分
            // =====================
            let base = values[item];

            // =====================
            // Step 3：streak
            // =====================
            if (item === prevItem) {
                streak++;
            } else {
                streak = 0;
            }

            score = base + streak;

            prevItem = item;
        }
        // =====================
        // Step 4：multiplier
        // =====================
        let index = i + 1; // 转成从1开始

        let multiplier = 1;
        if (index % 5 === 0) {
            multiplier = Math.floor(index / 5) + 1;
        }

        // =====================
        // Step 5：累加
        // =====================
        total += score * multiplier;
    }
    return total;
}

getCleanupScore(["bottle", "straw", "shoe", "battery"])