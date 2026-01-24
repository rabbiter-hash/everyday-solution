
function isValidHex(str){
    /*
        *** Checks if a string is a valid CSS HEX Color. It must like below:
        * 1. #211;
        * 2. #321bfa;
        * :param s:
        * :return: true if the string is valid, false otherwise;
     */
    // 1. 判定是否是字符串
    if (typeof str !== "string") return false;

    // 2. 正则返回
    const pattern = /^#([0-9a-fA-F]{3}|[a-fA-F0-9]{6})$/
    return pattern.test(str);
}

console.log(isValidHex("#331"));