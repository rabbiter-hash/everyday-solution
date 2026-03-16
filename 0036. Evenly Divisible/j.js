/* ==========================================
    第一种解法：取模法
 ========================================== */
function isEvenlyDivisible(a, b){
    // 1. 判定数据合法性
    if(!Number.isInteger(a) || !Number.isInteger(b)){
        throw new TypeError("A and B must be integers!");
    }
    // 2. b(divisor)不能是0
    if(b === 0){
        return false;
    }

    // 3. return
    return a % b === 0;
}
/* ==========================================
    第二种解法：更工程化写法
 ========================================== */
function isEvenlyDivisibleN(a, b){
    // 1. 判定数据合法性
    if(!Number.isInteger(a) || !Number.isInteger(b)){
        throw new TypeError("A and B must be integers!");
    }
    return b !== 0 && a % b === 0;
}
