# -*- encoding: utf-8 -*- 
# @Time: 2026/7/17 11:57
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: index.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def pig_latin(s):
    # 定义元音字母集合（小写）
    vowels = 'aeiou'

    # 将输入字符串按空格分割成单词列表
    words = s.split()

    # 存储转换后的单词
    result_words = []

    # 遍历每个单词
    for word in words:
        # 存储连续的辅音字母
        consonant_cluster = ''

        # 记录当前检查到的位置
        i = 0

        # 循环找出所有连续的开头辅音字母
        # 条件：位置小于单词长度 且 当前字母（转小写后）不是元音
        while i < len(word) and word[i].lower() not in vowels:
            consonant_cluster += word[i]  # 将辅音字母添加到辅音簇中
            i += 1  # 移动到下一个位置

        # 情况1：所有字母都是辅音（如 "fly"）
        if i == len(word):
            # 直接在单词末尾添加 "ay"
            converted = word + 'ay'

        # 情况2：以元音开头（i == 0 表示没有移动任何辅音）
        elif i == 0:
            # 直接在单词末尾添加 "way"
            converted = word + 'way'

        # 情况3：以辅音开头（有辅音簇需要移动）
        else:
            # 从第一个元音开始的部分 + 辅音簇 + "ay"
            converted = word[i:] + consonant_cluster + 'ay'

        # 处理大小写：保留原始单词首字母的大小写
        if word and word[0].isupper():
            # 如果原始首字母是大写，转换后的首字母也大写，其余小写
            converted = converted[0].upper() + converted[1:].lower()
        else:
            # 如果原始首字母是小写，转换后的首字母也小写，其余小写
            converted = converted[0].lower() + converted[1:]

        # 将转换后的单词添加到结果列表中
        result_words.append(converted)

    # 用空格将所有转换后的单词连接成字符串并返回
    return ' '.join(result_words)


pig_latin("universe")
pig_latin("hello")