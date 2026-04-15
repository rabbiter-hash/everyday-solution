
function getLastLetter(str){
    // 1. 通过正则取到字母列表
    const letters = str.match(/[a-zA-Z]/gi);

    // 2. 通过map转小写，并通过reduce累加取得最大值
    const maxChar = letters
        .map(ch => ch.toLowerCase())
        .reduce((a, b) => a > b ? a : b);

    // 3. 再次循环，使用小写对比
    for(let ch of letters){
        if(ch.toLowerCase() === maxChar){
            return ch;
        }
    }
}

getLastLetter("!#$ er@R asd fT.,> 2t0e9")