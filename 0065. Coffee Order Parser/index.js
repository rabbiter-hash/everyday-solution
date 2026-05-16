
function formatCoffeeOrder(order) {
    // 1. 转换成小写
    let orderStr = order.toLowerCase();

    console.log(orderStr);

    // 2. 将菜品和价格做成结构化数据
    const mapping = {
        "cold brew": 4.50,
        "oat latte": 5.00,
        "cappuccino": 4.75,
        "espresso": 3.00,
        "vanilla syrup": 0.75,
        "caramel drizzle": 0.60,
        "extra shot": 0.50,
        "oat milk": 0.75,
        "cream": 0.75,
    }

    // 3. 初始化存储
    let items = [];
    let total = 0;

    // 4. 循环
    for(let item in mapping){
        // 判定是否存在orderStr
        if(orderStr.includes(item)){
            // 说明存在，添加到数组
            items.push(item);

            // 将价格进行累加
            total += mapping[item];
        }
    }
    console.log(items);
    console.log(total);
    console.log(items.join(" + ") + ": " + "$" + total);
    console.log(items.join(" + ") + ": " + "$" + total.toFixed(2));
    return `${items.join(" + ")}: %$${total.toFixed(2)}`;
}

formatCoffeeOrder("I'd like an oat latte with vanilla syrup and an extra shot please.")