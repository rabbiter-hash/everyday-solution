
function transpose(matrix){
    // 1. 空矩阵处理
    if(matrix.length === 0) return [];

    // 2. 获取矩阵的行和列，假设列的长度是一样的
    const lenRow = matrix.length;
    const lenCol = matrix[0].length;

    console.log(lenRow);
    console.log(lenCol);

    // 3. 初始化一个矩阵
    const transposeArray = Array.from({length: lenCol}, () => Array.from(lenRow));

    console.log(transposeArray);
    // 4. 开始遍历
    for(let i = 0; i < lenRow; i++){
        for(let j = 0; j < lenCol; j++){
            transposeArray[j][i] = matrix[i][j];
        }
    }
    console.log(transposeArray);
    return transposeArray;
}

transpose([[1, 2, 3], [4, 5, 6]])

function tranposeIdiomatic(matrix) {
    return matrix[0].map((_, colIndex) => {
        return matrix.map(row => row[colIndex]);
    });
}