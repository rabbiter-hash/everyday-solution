function stripTags(html){
    // 1. 初始化结果集，直接用字符串
    let results = '';

    // 2. 初始化状态
    let status = false;

    // 3. 开始循环
    for(let ch of html){
        // 判定三种状态
        // 判定是否是html开始标签
        if(ch === "<") {
            // 更改状态值
            status = true;
        } else if(ch === ">") {
            // 如果到达了结束标签，就让状态回归false
            status = false;
        } else if(!status) {
            // 取反
            results += ch;
        }
        console.log(ch, status);
    }
    console.log(results);
    return results;
}

stripTags('<a href="#">Click here</a>')

