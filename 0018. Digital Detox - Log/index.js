
function digtialDetox(logs){
    // 1. 判定数据输入类型
    if(!Array.isArray(logs)){
        throw new TypeError("输入的不是数组！");
    }

    // 2. 输入处理
    const times = logs
        .map( t => new Date(t))
        .sort((a, b) => a - b);
    console.log(times);
    // 3. 定义条件
    const dayCounts = {}; // 字典统计出现次数
    const FOUR_HOURS = 4 * 60 * 60 * 1000; // 毫秒级4小时

    // 4. 遍历循环比较，注意边界问题
    for(let i = 0; i < times.length; i++){
        console.log("查看边界是否有undefined：", i + "===>" + times[i]);
        // 没有undefined，就校验条件一
        if(i > 0 && times[i] - times[i - 1] < FOUR_HOURS){
            return false;
        }

        // 条件二校验
        const day = times[i].toLocaleDateString("en-US");
        // 如果使用toISOString()，那么返回的是UTC时间，与要求不符
        // 注： 在进行日志校验的时候，服务器时区是首选
        dayCounts[day] = (dayCounts[day] || 0) + 1; // 没有就取0，每循环一次+1
        if(dayCounts[day] > 2) {
            return false;
        }
    }
    return true;
}

console.log(digitalDetox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]))