/* ==========================================
    第一种解法：常规遍历法将值替换
 ========================================== */
function invertMatrix(matrix) {
    // 1. 找到两个值
    const values = new Set();
    matrix.forEach(row => {
        row.forEach(cell => {
            values.add(cell);
        })
    });
    console.log(values); //Set(2) { 'a', 'b' }

    const [v1, v2] = [...values];
    console.log(v1, v2);

    // 2. 构建新矩阵
    return matrix.map(row => row.map(cell => (cell === v1 ? v2 : v1)));
}

console.log(invertMatrix([["a", "b"], ["a", "a"]]));