
function navigateTrail(map){
    // 1. 判定是否是数组
    if(!Array.isArray(map)){
        throw new Error("输入必须是数组！");
    }

    // 2. 转成二维数组
    const grid = map.map(item => item.split(""));
    console.log(grid);
    // rows
    const rows = grid.length;
    const cols = grid[0].length;

    let r0, c0;
    // 3. 找到c的位置
    for(let r=0; r < rows; r++){
        for(let c = 0; c < cols; c++){
            if(grid[r][c] === "C"){
                r0 = r;
                c0 = c;
            }
        }
    }
    let r = r0;
    let c = c0;

    let prevStep = null;
    let path = "";

    // 4. 开始循环
    while(grid[r][c] !== "G"){

        // 相邻坐标
        const neighbors = [
            [r, c + 1, "R"],
            [r + 1, c, "D"],
            [r, c - 1, "L"],
            [r - 1, c, "U"]
        ];

        // 循环
        for (let [nr, nc, moveDirection] of neighbors){
            if(
                nr >= 0 &&
                nr < rows &&
                nc >= 0 &&
                nc < cols &&
                ["T", "G"].includes(grid[nr][nc]) &&
                (prevStep === null || !(nr === prevStep[0] && nc === prevStep[1]))
            ) {
                path += moveDirection;
                // 更新前一步的数值
                prevStep = [r, c];
                // 更新当前坐标
                r = nr;
                c = nc;
                break; // 必须满足条件才退出循环
            }
        }
    }
    return path;
}

console.log(navigateTrail(["-CT--", "--T--", "--TT-", "---T-", "---G-"]))