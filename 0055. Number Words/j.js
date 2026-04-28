
function getNumberWords(n){
    // 1. 编码20以下的数字
    const words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    ];

    // 2. 编码整数，因为要从输入整除，所以0和10都要编码为空码
    const tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty",
        "seventy", "eighty", "ninety"
    ];

    // 3. 开始判定20以下的
    if(n < 20){
        // 直接以输入为索引进行提取
        return words[n];
    }

    // 4. 判定是否整除
    let ten = Math.floor(n / 10); // 十位数，需要用来作为提取十位数的索引
    let one = n % 10; // 个位数

    if(one === 0){
        // 说明是整数，就需要用到ten来提取数值
        return tens[ten];
    }

    return tens[ten] + "-" + words[one];
}