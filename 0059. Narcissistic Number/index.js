
function isNarcissistic(n) {
    // 1. 判定数据输入的合法性
    if(!Number.isInteger(n)){
        throw new TypeError("输入必须是整数！");
    }

    // 2. 将数字转成字符串
    const str = String(n);
    console.log(str);

    const power = str.length;
    // 3. 初始化计量结果
    let total = 0;

    // 4. 循环
    for(let i = 0; i < str.length; i++){
        // 定义数字
        const digit = Number(str[i]);
        console.log(digit);

        // 累加和
        total += Math.pow(digit, power);
        console.log(total);
    }
    console.log(total);

    // 5. 判定是否相等
    if(total === n){
        return true;
    }

    return false;
}

// isNarcissistic(153)

function isNarcissisticIdiomatic(n){
    const digits = String(n).split("");
    console.log(digits);
    const power = digits.length;

    return n === digits.reduce(
        (acc, num) => acc + Math.pow(num, power), 0
    );
}

isNarcissisticIdiomatic(153)