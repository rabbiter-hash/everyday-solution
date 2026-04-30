
function isInCrossword(char){
    // 1. 矩阵
    const grid = [
            [0, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 0, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 0]
    ];

    // 2. 字符八位二进制
    const target = char.charCodeAt(0).toString(2).padStart(8, "0");
    /*
        说明：
        1. charCodeAt(0)：获取字符的Unicode码点，类似python的ord
            "a".charCodeAt(0) = 97
        2. toString(2)：将数字转换成二进制字符串；
            97.toString(2) = "1100001"（注意：没有前导0）
        3. padStart(8, "0")：在字符串开头补0，确保长度至少为8位
            "1100001".padStart(8, '0') → "01100001"
     */
    console.log(target, target.length);

    // 3. 横向循环矩阵，取row跟目标对比
    for(let i = 0; i < grid.length; i++){
        // console.log(grid[i]); // array
        const row = grid[i];
        const rowStr = row.join("");
        // console.log(rowStr);
        // console.log(typeof rowStr); //string
        if(
            rowStr === target ||
            rowStr.split("").reverse().join("") === target
        ) return true;
    }

    console.log("开始纵向循环准备！");
    // 4. 纵向循环，纵向循环先要固定列的位置，然后去取行的值
    // console.log(grid);
    for(let p = 0; p < grid.length; p++){
        // 先固定列数的值，然后去取行的值
        let colStr = "";
        for(let q = 0; q < grid.length; q++){
            colStr += grid[q][p];
            // console.log(colStr);
        }
        console.log(colStr);
        // 5. 等构造出完整八位字符串再去比较
        if(
                colStr === target ||
                colStr.split("").reverse().join("") === target
            ) return true;
    }
    return false;
}

isInCrossword("abc");


