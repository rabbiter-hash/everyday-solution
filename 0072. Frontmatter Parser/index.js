function parseFrontmatter(str) {
    // 初始化结果集
    let result = {};

    // 先取出字符串中的行
    const lines = str.split("\n").slice(1, -1);
    // console.log(lines);

    // 开始循环
    for(const line of lines){
        // console.log(line);
        // 这里需要特别注意的是，需要取到第一个冒号的前后，值有可能会出现网址，那就会有两个冒号
        const firstDelimiter = line.indexOf(":", 1);

        const key = line.slice(0, firstDelimiter);
        // console.log(key);
        let value = line.slice(firstDelimiter + 1, ).trim();
        console.log(value);

        // 开始处理值的情况
        if(value === "true"){
            value = true;
        } else if(value === "false"){
            value = false;
        } else if(!Number.isNaN(Number(value))){
            // 如果 value 能够被转换成合法的数字（转换结果不是 NaN），就把它转换成 Number 类型。
            value = Number(value);
        }
        result[key] = value;
    }

    console.log(result);
    return result;
}
parseFrontmatter("---\ntitle: My Post\ndraft: false\nviews: 100\n---");
parseFrontmatter("---\nversion: 1.0.0\nurl: https://example.com\nprivate: true\n---")