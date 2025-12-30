


function stringSum(s){
    // 1. 全局正则提取数字
    let result_digits = s.match(/\d+/g);

    // 2. 初始加和
    if (!digits_results) return 0;

    // 3. 开始处理
    let total = 0;
    for(let i=0; i<result_digits.length; i++){
        // console.log(result_digits[i]);
        total += Number(result_digits[i]);
    }
    return total;
}



// 上述办法有点python化，js一般是链式调用比较多
function stringSumJS(s) {
    return (s.match(/\d+/g) || [])
        .reduce((sum, n)=>sum + Number(n), 0);
}