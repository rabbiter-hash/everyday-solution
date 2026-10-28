function sequence(n) {
    // 1. 存储结果集
    let result = '';

    // 2. 开始循环
    for (let i = 1; i <= n; i++){
        console.log(i);
        result += String(i);
    }

    console.log(result);
    return result;
}

sequence(5)

function sequenceArrayFrom(n) {
    return Array.from(
        {length: n},
        (_, i) => i + 1
    ).join('');
}
