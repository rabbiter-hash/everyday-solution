/* ==========================================
    第一种解法：循环遍历
 ========================================== */
function capitalizeFibonacci(str){
    // 1. 计算字符串的长度
    let maxIndex = str.length - 1;
    console.log(maxIndex);

    // 2. 斐波那契数列集合处理
    let a = 0, b = 1;
    let fibsSet = new Set();
    while( a <= maxIndex ){
        fibsSet.add(a);
        [a, b] = [b, a + b];
    }

    let result = "";
    // 3. 循环
    for(let i = 0; i < str.length; i++){
        // 这里要用str.length
        const char = str[i];
        if(fibsSet.has(i)){
            // 正则处理
            result += /[a-zA-Z]/.test(char)
        }
    }
}

capitalizeFibonacci("hello world")
capitalizeFibonacci("HELLO WORLD")