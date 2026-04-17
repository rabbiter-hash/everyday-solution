
function getInitials(name){
    // 1. 判定数据是否合法
    if(typeof name !== "string"){
        throw new Error("输入必须是字符串！");
    }

    // 2. 以空格拆分字符串
    // const nameWords = name.split(" ");
    // 2. js强调用户输入，所以需要用trim()处理两边，并处理多空格问题
    const nameWords = name.trim().split(/\s+/);

    // 3. 初始化存储结果
    let nameInitials = [];

    // 4. 开始遍历，并取每个单次的首个字母的大写
    for(let i = 0; i < nameWords.length; i++){
        nameInitials.push(nameWords[i][0].toUpperCase());
    }
    // console.log(nameInitials.join(".") + ".");
    return nameInitials.join(".") + ".";
}

getInitials("Dorothy Vera Clump Haverstock Norris")

function getInitialsSimple(name){
    return name
        .trim()
        .split(/\s+/)
        .map(word => word[0].toUpperCase())
        .join(".") + ".";
}