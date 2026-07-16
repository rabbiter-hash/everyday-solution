function getMaxProfit(prices, budget){
    // 1. 初始化最大利润和最大天数
    let maxProfit = 0;
    const maxDays = prices.length;

    // 2. 开始循环
    for(let i = 0; i < maxDays - 1; i++){
        for(let j = i+1; j < maxDays; j++){
            // 取出当前循环的买入价和卖出价
            const buyPrice = prices[i];
            const sellPrice = prices[j];

            // 只有当卖出价大于买入价的时候，才有利可图
            if(sellPrice > buyPrice){
                // 计算可购买股数
                const shares = Math.floor(budget / buyPrice);

                // 计算利润
                const profit = shares * (sellPrice - buyPrice);

                // 更新最大利润
                if(profit > maxProfit){
                    maxProfit = profit;
                }
            }
        }
    }
    console.log(maxProfit);
    // 向下取整保留两位小数
    const results = Math.floor(maxProfit * 100) / 100;
    console.log(results);
    // 保留两位小数
    return results.toFixed(2);
}

getMaxProfit([8, 2, 5, 10], 20)