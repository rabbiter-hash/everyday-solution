function daysUntilBirthday(today, birthday) {
    // 1. 解析今天的日期 (YYYY-MM-DD)
    const todayParts = today.split('-').map(Number);
    const todayDate = new Date(todayParts[0], todayParts[1] - 1, todayParts[2]);
    const year = todayDate.getFullYear();

    // 2. 解析生日 (M/D)
    const birthdayParts = birthday.split('/').map(Number);
    const month = birthdayParts[0];
    const day = birthdayParts[1];

    // 3. 辅助函数：查找下一个有效日期（处理2/29等特殊情况）
    function findNextValidDate(startYear, targetMonth, targetDay) {
        let year = startYear;
        while (true) {
            const testDate = new Date(year, targetMonth - 1, targetDay);
            // 检查日期是否有效（月份和日期是否匹配）
            if (testDate.getMonth() === targetMonth - 1 &&
                testDate.getDate() === targetDay) {
                return testDate;
            }
            year++;
        }
    }

    // 4. 构造今年的生日
    let nextBirthday;
    const thisYearBirthday = new Date(year, month - 1, day);
    const isValidThisYear = (thisYearBirthday.getMonth() === month - 1 &&
                             thisYearBirthday.getDate() === day);

    if (isValidThisYear) {
        // 今年生日存在
        const todayMidnight = new Date(year, todayDate.getMonth(), todayDate.getDate());
        const birthdayMidnight = new Date(year, month - 1, day);

        if (birthdayMidnight > todayMidnight) {
            // 今年的生日还没到
            nextBirthday = birthdayMidnight;
        } else {
            // 今天就是生日或者生日已过，找明年的
            nextBirthday = findNextValidDate(year + 1, month, day);
        }
    } else {
        // 今年没有这个生日（比如2/29在非闰年）
        nextBirthday = findNextValidDate(year + 1, month, day);
    }

    // 5. 计算天数差（向上取整，确保得到完整天数）
    const diffTime = nextBirthday.getTime() - todayDate.getTime();
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

    return diffDays;
}

