function sumDivisors(n){
    let sum = 0;
    if(n <=0 ) return;
    for(let i=1;i<=n;i++){
        // 注意从1开始
        if(n % i === 0){
            sum += i;
        }
    }
    return sum;
}

function sumDivisorsSqrt(n){
    let sum = 0;
    if(n <= 0) return;
    for(let i=1;i<=Math.sqrt(n);i++){
        // 防止平方数重复加
        if(n % i === 0){
            sum += i;
            if(i !== n / i){
                sum += n / i;
            }
        }
    }
    return sum;
}



