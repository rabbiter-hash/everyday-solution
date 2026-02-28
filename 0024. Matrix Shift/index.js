
function matrixShift(matrix, shift){
    // 1. 判定数据是否合法
    if(!Array.isArray(matrix)){
        throw new Error("matrix必须是数组！");
    }
    if(!Number.isInteger(shift)) {
        throw new Error("Shift必须是整数！");
    }
    // 2. 数组信息
    const matrixRows = matrix.length;
    const matrixCols = matrix[0].length;
    console.log(matrixRows, matrixCols);
    // 数组长度
    const n = matrixRows * matrixCols;
    // 3. 处理shift，不同于python
    shift = ((shift + n) % n) % n; // 这一步保证负数也能正确
    console.log(shift);
    // 4. 扁平化数组
    const flat = matrix.flat();
    console.log(flat);
    // 5. 根据shift移动数组
    const shifted = flat.slice(-shift).concat(flat.slice(0, -shift));
    console.log(shifted);
    // 6. 返回结果
    const result = []
    for(let i = 0; i < matrixRows; i++) {
        const start = i * matrixCols;
        const end = start + matrixCols;
        // result.push(shifted.slice(start, end));
        // 也可以写成
        result.push(shifted.slice(i * matrixCols, (i+1) * matrixCols));
    }
    return result;
}

console.log(matrixShift([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], 1))