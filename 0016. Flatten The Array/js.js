
function flattenArray(arr) {
    if(!Array.isArray(arr)) {
        throw new TypeError("请输入数组！");
    }

    // 1. 展开运算符拷贝，避免破坏原数组
    const stack = [...arr];
    // 结果
    const result = [];

    // 2. 开始迭代循环
    while(stack.length) {
        // 从栈顶取出
        const next = stack.pop();
        if(Array.isArray(next)){
            // 如果是数组，压入到stack
            stack.push(next);
        } else {
            // 如果不是数组，就存储结果
            result.push(next);
        }
    }
    // 栈是LIFO，需要翻转数组
    return result.reverse();
}

console.log(['a', [[[[['nb']]]]]], ['c']);