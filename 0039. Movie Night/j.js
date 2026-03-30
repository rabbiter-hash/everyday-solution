/* ==========================================
    第一种解法：循环遍历
 ========================================== */
function getMovieNightCost(day, showtime, numberOfTickets){
    // 1. 周二要覆盖所有规则
    if(day === "Tuesday"){
        return `$${(5 * numberOfTickets).toFixed(2)}`;
    }

    // 2. 基础票价
    let price;
    if(["Friday", "Saturday", "Sunday"].includes(day)){
        price = 12;
    } else {
        price = 10;
    }

    // 3. 解析时间，例如4:30
    let [hourPart, minutePart] = showtime.split(":");
    let hour = parseInt(hourPart);
    let minute = parseInt(minutePart.slice(0, 2));
    let period = minutePart.slice(2);

    // 4. 转24小时
    if(period === "pm" && hour !== 12){
        hour += 12;
    }
    if(period === "am" && hour === 12){
        hour = 0;
    }

    // 5. 午场判断
    if(hour < 17){
        price -= 2;
    }

    // 6.总价
    let total = price * numberOfTickets;

    return `$${total.toFixed(2)}`;
}

/* ==========================================
    第二种解法：用Date，更原生
        隐患：Date解析不稳定
        let date = new Date(`1970-01-01 ${showtime}`);
        这里有个坑：
        JavaScript 对 "4:00pm" 这种格式：
            不是标准 ISO 格式
            在不同环境（浏览器 / Node.js）可能解析失败
            能出现的情况
        new Date("1970-01-01 4:00pm")
        有的环境会得到：
        Invalid Date
 ========================================== */
function getMovieNightCostDate(day, showtime, numberOfTickets){
    // 1. 周二直接返回
    if (day === "Tuesday") {
        return `$${(5 * numberOfTickets).toFixed(2)}`;
    }

    // 2. 价格
    let price = ["Friday", "Saturday", "Sunday"].includes(day) ? 12 : 10;

    // 3. 用 Date 解析时间
    let date = new Date(`1970-01-01 ${showtime}`);

    // 4. 午场
    if (date.getHours() < 17) {
        price -= 2;
    }

    return `$${(price * numberOfTickets).toFixed(2)}`;
}


function getMovieNightCostMapping(day, showtime, numberOfTickets){
    const basePrice = {
        Monday: 10,
        Tuesday: 5,
        Wednesday: 10,
        Thursday: 10,
        Friday: 12,
        Saturday: 12,
        Sunday: 12
    };

    let price = basePrice[day];

    if (day === "Tuesday") {
        return `$${(price * numberOfTickets).toFixed(2)}`;
    }

    let hour = parseInt(showtime.split(":")[0]);
    let period = showtime.slice(-2);

    if (period === "pm" && hour !== 12) hour += 12;
    if (period === "am" && hour === 12) hour = 0;

    if (hour < 17) price -= 2;

    return `$${(price * numberOfTickets).toFixed(2)}`;
}