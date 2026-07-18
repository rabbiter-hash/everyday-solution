function chunkArray(arr, size) {
    // 1. 初始化结果集
    let results = [];

    // 2. 循环遍历
    for(let i = 0; i < arr.length; i+=size){
        results.push(arr.slice(i, i+size));
    }

    console.log(results);
    return results;
}


function chunkArrayWhile(arr, size) {
    const result = [];
    let i = 0;
    while (i < arr.length) {
        result.push(arr.slice(i, i + size));
        i += size;
    }
    return result;
}