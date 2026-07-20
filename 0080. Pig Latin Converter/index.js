/**
 * 将字符串转换为Pig Latin
 * @param {string} s - 需要转换的字符串
 * @returns {string} 转换后的Pig Latin字符串
 */
function pigLatin(s) {
    // 定义元音字母集合（小写）
    const vowels = 'aeiou';

    // 将输入字符串按空格分割成单词数组
    const words = s.split(' ');

    // 存储转换后的单词
    const resultWords = [];

    // 遍历每个单词
    for (let word of words) {
        // 存储连续的辅音字母
        let consonantCluster = '';

        // 记录当前检查到的位置
        let i = 0;

        // 循环找出所有连续的开头辅音字母
        // 条件：位置小于单词长度 且 当前字母（转小写后）不是元音
        while (i < word.length && !vowels.includes(word[i].toLowerCase())) {
            consonantCluster += word[i];  // 将辅音字母添加到辅音簇中
            i++;  // 移动到下一个位置
        }

        let converted;

        // 情况1：所有字母都是辅音（如 "fly"）
        if (i === word.length) {
            // 直接在单词末尾添加 "ay"
            converted = word + 'ay';
        }
        // 情况2：以元音开头（i === 0 表示没有移动任何辅音）
        else if (i === 0) {
            // 直接在单词末尾添加 "way"
            converted = word + 'way';
        }
        // 情况3：以辅音开头（有辅音簇需要移动）
        else {
            // 从第一个元音开始的部分 + 辅音簇 + "ay"
            converted = word.slice(i) + consonantCluster + 'ay';
        }

        // 处理大小写：保留原始单词首字母的大小写
        if (word && word[0] === word[0].toUpperCase()) {
            // 如果原始首字母是大写，转换后的首字母也大写，其余小写
            converted = converted[0].toUpperCase() + converted.slice(1).toLowerCase();
        } else {
            // 如果原始首字母是小写，转换后的首字母也小写，其余小写
            converted = converted[0].toLowerCase() + converted.slice(1);
        }

        // 将转换后的单词添加到结果数组中
        resultWords.push(converted);
    }

    // 用空格将所有转换后的单词连接成字符串并返回
    return resultWords.join(' ');
}