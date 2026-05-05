function convertParsecs(parsecs){
    // 1. 判定数据输入的合法性
    if(!Number.isInteger(parsecs)){
        throw new Error("输入必须是整数！");
    }

    // 2. 返回
    return parsecs % 2 === 0 ? parsecs * (6 / 2) : parsecs * 2;
    // 更简洁
    // return parsecs * (parsecs % 2 === 0 ? 3 : 2);
}