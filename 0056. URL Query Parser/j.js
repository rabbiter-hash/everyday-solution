
function parseUrlQuery(url) {
    // 1. 初始化结果存储
    const results = {};

    // 2. 用 ? 分割取后面部分
    const query = url.split("?")[1];
    console.log(query);
    // 3. 用 & 取参数部分
    const params = query.split("&");
    console.log(params);
    for(let param of params){
        const [key, value] = param.split("=");
        results[key] = value;
    }

    return results;
}

parseUrlQuery("https://example.com/search?name=Alice&age=30")

console.log(new URL("https://example.com/search?name=Alice&age=30"));