
function zipStrings(a, b){
    // 1. 结果集
    let result = '';

    // 2. 取最短长度
    let minLength = Math.min(a.length, b.length);

    // 3. 循环
    for(let i = 0; i < minLength; i++){
        result += a[i] + b[i];
    }
    console.log(result);

    // 4. 继续追加长度
    result += a.slice(minLength, ) + b.slice(minLength, );

    console.log(result);

    return result;
}

zipStrings("python", "javascript")