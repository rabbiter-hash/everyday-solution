function roundToNearestMultiple(num, multiple) {
    // 1. 先算商
    const quotient = Math.floor( num / multiple );
    // 2. 余数
    const remainder = num % multiple;

    // 3. 比较
    if(remainder < multiple / 2){
        return quotient * multiple;
    } else {
        return (quotient + 1 ) * multiple;
    }
}