function markdownImageParser(markdown){

    // 1. 正则规则
    const reg = /!\[([^\]]+)\]\(([^)]+)\)/;
    // 2. 解构
    const [, alt, src] = markdown.match(reg);

    console.log(alt);
    return `<img src="${src}" alt="${alt}">`;

}

