# -*- encoding: utf-8 -*- 
# @Time: 2026/4/24 14:09
# @Author: 一叶孤城
# @Email: 28104511@qq.com
# @File: p.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)


def compress(s):
    # 1. 将字符串单词转成数组
    words_arr = s.split()

    # 2. 存储结果集
    ## 2.1、哈希表存储每个单词第一次出现的位置
    word_map = {}
    ## 2.2、结果集存储最终结果
    result = []

    # 3. 循环遍历
    for i,word in enumerate(words_arr):
        # 需要要判定是否在哈希表中
        if not word in word_map:
            # 不存在就要创建哈希表，注意+1的问题
            word_map[word] = i + 1
            # 将word追加到列表
            result.append(word)
        else:
            # 否则就是已经存在哈希表中了，直接append当前word在哈希表中的位置数值
            result.append(str(word_map[word]))

    return " ".join(result)

compress("the cat sat on the mat on which the cat sat")


def compress_pythonic(s):
    seen = {}
    return " ".join(
        seen.setdefault(word, str(i+1)) if word in seen else word
        for i, word in enumerate(s.split())
    )