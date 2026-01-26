/* ==========================================
    第一种解法：常规解法，根据题目要求依次写代码
 ========================================== */
function scaleImage(size, scale){
    // 1. 数据判定
    if(typeof size !== "string" || typeof scale !== 'number'){
        throw new TypeError("Invalid input!");
    }

    // 2. 解构赋值，得到字符串
    const [width, height] = size.split('x').map(Number);
    console.log(width, height, typeof width, typeof height); // 1200 720 number number

    // 3. 直接返回
    return `${width * scale}x${height * scale}`;
}
console.log(300 * 1.5); // 450
console.log(scaleImage("1200x720", 1.5))

/* ==========================================
    第二种解法：正则解法、校验即解析
 ========================================== */
function scaleImageRe(size, scale) {
    console.log("第二种解法：==============================")
    // 1. 判定输入
    if(typeof size !== "string" || typeof scale !== "number"){
        throw new TypeError("Invalid input!");
    }

    // 2. 正则解析
    const pattern = /^(\d+)x(\d+)$/;
    const match = size.match(pattern);
    console.log("得到的正则匹配结果为：", match);
    if(!match) {
        throw new Error("Invalid size format!");
    }

    // 3. 解构赋值
    const [ , width, height] = match.map(Number);
    console.log(width, height, typeof width, typeof height);

    // 4. 返回
    return `${width * scale}x${height * scale}`;
}

console.log(scaleImageRe("1920x1080", 1.5))

/* ==========================================
    第三种解法：replace + 回调
 ========================================== */
function scaleImageReplace(size, scale) {
    console.log("第三种解法：==============================");
    // 1. 输入校验
    if(typeof size !== "string" || typeof scale !== "number") {
        throw new TypeErorr("Invalid input!");
    }

    // 2. 正则校验
    if(!/^(\d+)x(\d+)$/.test(size)){
        throw new Error("Invalid size format!");
    }

    // 3. 直接返回
    return size.replace(/\d+/g, n => Number(n) * scale);
}

console.log(scaleImageReplace("1270x720", 1.5));

/* ==========================================
    第四种解法：函数式 map + join
 ========================================== */
function scaleImageFunction(size, scale) {
    console.log("第四种解法：=============================");
    // 1. 数据输入判定
    if(typeof size !== "string" || typeof scale !== "number"){
        throw new TypeError("Invalid input!");
    }

    // 2. 求值
    const values = size.split("x").map(Number);
    console.log(values);

    // 3.判定size值是否合法
    if(values.length !== 2 || values.some(v => !Number.isInteger(v))){
        throw new Error("Invalid size format!");
    }

    // 4. 返回
    return values.map(v => v * scale).join("x");
}
console.log(scaleImageFunction("1920x1080", 1.5));