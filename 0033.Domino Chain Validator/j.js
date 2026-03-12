/* ==========================================
    第一种解法：循环遍历
 ========================================== */
function isValidDominoChain(dominoes){
    /*
    * @params: dominoes
    * @returns: true or false
    * @methods: use for directly
    * */
    // 1. Input check
    // 1.1. The Value of input must be an array
    if(!Array.isArray(dominoes)){
        throw new Error("Input value must be an array!")
    }
    // 1.2. Inner Array check
    for(let domino of dominoes){
        if(!Array.isArray(domino)){
            throw new Error("Inner element must be an array!");
        }
        // check the inner element's length
        if(domino.length !== 2){
            throw new Error("Inner array length must be 2")
        }
        // check the inner array's element is integer
        for(let d of domino){
            if(!Number.isInteger(d) || (d < 1 && d > 6)){
                throw new Error("Inner arrays' elements' must be integer!");
            }
        }
    }

    // 2. Use for loop to check the value
    for(let i = 0; i < dominoes.length - 1; i++){
        // The behavior -1 is a must have.
        if(dominoes[i][1] !== dominoes[i+1][0]){
            return false;
        }
    }
    return true;
}
isValidDominoChain([[1, 3], [3, 6], [6, 5]])

/* ==========================================
    第二种解法：使用every函数
 ========================================== */
function isValidDominoChainWithEvery(dominoes){
    return dominoes.every((domino, i) =>
        // domino是当前骨牌，而下一骨牌是dominoes[i+1]
        i === dominoes.length - 1 || domino[1] === dominoes[i+1][0]
    )
}
isValidDominoChainWithEvery([[1, 3], [3, 6], [6, 5]])

/* ==========================================
    第三种解法：slice + every
 ========================================== */
function isValidDominoChainWithSlicePlusEvery(dominoes){
    return dominoes
        .slice(0, -1)
        .every((domino, i) => domino[1] === dominoes[i+1][0]);
}
isValidDominoChainWithSlicePlusEvery([[1, 3], [3, 6], [6, 5]])