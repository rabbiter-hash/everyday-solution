function validate(email) {
    // 1. 检查是否包含@，没有就return false
    let atIndex = email.indexOf("@");
    console.log(atIndex);
    console.log(email.lastIndexOf("@"));
    // 判定@的数量和位置
    if((atIndex === -1) || atIndex !== email.lastIndexOf("@")) {
        return false;
    }
    // 2. 通过@拆分成localpart和domain part
    let localPart = email.slice(0, atIndex);
    let domainPart = email.slice(atIndex + 1, );
    console.log(localPart);
    console.log(domainPart);

    // 如果local和domain都为空，肯定不是正确的
    if((localPart === '') || (domainPart === '')) {
        return false;
    }
    // 3. 检查localpart部分
    // 3.1、检查localPart的点的位置
    if((localPart.startsWith('.')) || localPart.endsWith('.')) {
        return false;
    }
    // 3.2、判定是否有连续的..
    if(localPart.includes('..')) {
        return false;
    }
    // 3.3、检查local的每个字符
    for(let i = 0; i < localPart.length; i++){
        let char = localPart[i];
        // console.log(char);
        let isLetter = (
            (char >= 'a' && char <= 'z') ||
            (char >= 'A' && char <= 'Z')
        );
        let isDigit = (
            char >= '0' && char <= '9'
        );
        let isSymbol = (
            char === '.' ||
            char === '-' ||
            char === '_'
        );

        // 循环的每个字符都应该满足上面三个条件
        if(!isLetter && !isDigit && !isSymbol) {
            return false;
        }
    }
    // 4. 检查domain part部分
    // 4.1、domain part必须包含点，且不能有连续的点
    // console.log(domainPart.includes('.'));
    // console.log(domainPart.includes('..'));
    if(!domainPart.includes('.') || domainPart.includes('..')) {
        // 如果不不包含点或者包含两个点，直接false
        return false;
    }
    // 4.2、检查最后一个点后最少包含两个英文字母
    // 记得这里一定要用lastIndexOf
    let dotIndex = domainPart.lastIndexOf('.');
    let suffix = domainPart.slice(dotIndex + 1);

    // 4.3、如果点后的长度小于2，直接false
    if(suffix.length < 2) {
        return false;
    }

    //4.4、最后的两个字符必须是英文字母
    for(let i = 0; i < suffix.length; i++) {
        // 提取出字符
        let char = suffix[i];
        // 字母表达式
        let isLetter =
            (char >= 'a' && char <= 'z') ||
            (char >= 'A' && char <= 'Z');

        if (!isLetter) {
            return false;
        }
    }
    return true;
}

validate('john.doe_123@example.com'); // true
validate('.john@example.com');        // false
validate('john..doe@example.com');    // false
validate('john@example.c');           // false
validate('john@example..com');        // false
validate('john@example.com.cn');      // true

console.log("a".indexOf("bbb"))

console.log("bbbbcceafeadff".lastIndexOf("f"))