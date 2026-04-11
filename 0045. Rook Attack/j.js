
/* ==========================================
    第一种解法：常规解法
 ========================================== */
function rookAttack(rook1, rook2) {
    // 1. 首先还是做数据判定
    if(typeof rook1 !== "string" || typeof rook2 !== "string") {
        throw new TypeError("输入必须是字符串！");
    }

    if(rook1.length !== 2 || rook2.length !== 2){
        throw new Error("字符串长度必须为2！");
    }

    const col1 = rook1[0];
    const row1 = rook1[1];

    const col2 = rook[0];
    const row2 = rook2[1];

    return col1 === col2 || row1 === row2;
}

/* ==========================================
    第二种解法：一行解法
 ========================================== */
function rookAttackSingle(rook1, rook2){
    return rook1[0] === rook2[0] || rook1[1] === rook2[1];
}

/* ==========================================
    第三种解法：解构
 ========================================== */
function rookAttackDeconstruction(rook1, rook2){
    const [c1, r1] = rook1;
    console.log(c1);
    console.log(r1);
    const [c2, r2] = rook2;

    return c1 === c2 || r1 === r2;
}

/* ==========================================
    第四种解法：类似python的any
 ========================================== */
function rookAttackSome(rook1, rook2){
    return [...roo1].some((ch, i) => ch === rook2[i]);
}

