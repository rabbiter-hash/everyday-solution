
/* ==========================================
    第一种解法：常规解法
 ========================================== */
function getRotation(n) {
    // 1. 判定输入的合法性
    if(!Number.isInteger(n) || (n.toString()).includes("0") || n < 0){
        // 将数字n转成字符串用n.toString()
        throw new TypeError("N must be a positive integer and not contains 0");
    }

    // 2. 将数字转成字符串并提取长度
    const nStr = n.toString();
    let nLength = nStr.length;

    // 3. 开始循环
    for(let i = 0; i < nLength; i++){
        // console.log(i);
        // 旋转数字
        let rotatedNum = nStr.slice(i, nLength) + nStr.slice(0,i);
        // console.log(rotatedNum, typeof rotatedNum);
        if(rotatedNum % nLength === 0){
            // console.log(i, rotatedNum);
            return i;
        }
    }
    return "none";
}

console.log(getRotation(13579));