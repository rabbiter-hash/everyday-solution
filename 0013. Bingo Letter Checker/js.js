
/* ==========================================
    第一种解法：常规解法，用if...else if...else直接出结果
 ========================================== */
function getBingoLetterNormal(n){
    /* ==========================================
        1. 判定是否是数字；
        2. 数字在1-75之间；
        *** 3. js没有数学上的链式判断，也即：
            if(1<=n<=10)
            需要写成：
            if(n >= 1 && n <= 10)
     ========================================== */
    // 1. 判定是否是数字
    n = Number(n);

    if(Number.isNaN(n) || n < 1 || n > 75) {
        // isNaN: 其中NaN表示，Not A Number
        return "输入必须是数字且在1-75之间！";
    }
    // 2. 条件判断： 注意，js的没有数学中的链式
    if(n >=1 && n <= 15){
        return "B";
    } else if(n >= 16 && n <= 30){
        return "I";
    } else if(n >= 31 && n <= 45){
        return "N";
    } else if(n >= 46 && n <= 60){
        return "G";
    } else {
        return "O";
    }
}

/* ==========================================
    第二种解法：工程化
        B: 1 - 15
        I: 16 - 30
        N: 31 - 45
        G: 46 - 60
        O: 61 - 75
        每次相差15
 ========================================== */
function getBinggoLettersSimple(n){
    n = Number(n);
    if(Number.isNaN(n) || n < 1 || n > 75) {
        return "输入必须是数字且在1-75之间！";
    }
    const letters = ["B", "I", "N", "G", "O"];
    // 使用Math.floor向下取整；访问数组使用[]
    return letters[Math.floor((n-1) / 15)];
}

/* ==========================================
    第三种解法：map映射
 ========================================== */
function getBingoLettersMapping(n){
    // 1. 强制转换成数字
    n = Number(n);

    // 2. 判定是否是数字
    if(Number.isNaN(n) || n < 1 || n > 75) {
        return "invalid";
    }

    const mapping = new Map([
        [[1, 15], "B"],
        [[16, 30], "I"],
        [[31, 45], "N"],
        [[46, 60], "G"],
        [[61, 75], "O"],
    ]);

    for (const [[start, end], letter] of mapping){
        if(n >= start && n <= end){
            return letter;
        }
    }
}

/* ==========================================
    第四种解法：配置驱动映射
 ========================================== */
const BINGO_RULES = [
        [1, 15, "B"],
        [16, 30, "I"],
        [31, 45, "N"],
        [46, 60, "G"],
        [61, 75, "O"],
    ];
function getBingoLettersDriverMap(n){
    if(!Number.isInteger(n) || n < 1 || n > 75){
        return "invalid";
    }

    for (const [start, end, letter] of BINGO_RULES){
        console.log(start, end, letter);
        if(n >= start && n <= end) {
            return letter;
        }
    }
}