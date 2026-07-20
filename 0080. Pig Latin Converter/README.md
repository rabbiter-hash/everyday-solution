# Pig Latin Converter

Given a string, convert it to Pig Latin using the following rules:

- If a word begins with a vowel (`"a"`, `"e"`, `"i"`, `"o"`, or `"u"`), add `"way"` to the end. For example, `"universe"` converts to `"universeway"`.
- If a word begins with one or more consonants, move them to the end and add `"ay"`. For example, `"hello"` converts to `"ellohay"`.
- Preserve the case of the first letter. For example, `"Hello"` converts to `"Ellohay"`.

## 一、题解和思路

### 1.1、题解

如果输入以元音字母开头，就返回该字符+"way"，如果是辅音字母开头，就将辅音字母开头，就将所有辅音字母提取到字符串末尾并加上ay，返回的字符串需要以首字母大写开头。

### 1.2、思路

1. **判断首字母是否为元音**（a, e, i, o, u，不区分大小写）
   - 如果是：`原词 + "way"`
   - 如果否：进入第2步
2. **提取所有连续的开头辅音**
   - 从第一个字母开始，找到所有连续的辅音字母
   - 将这些辅音移到末尾，再加上 "ay"
3. **大小写处理**
   - 返回结果的第一个字母大写，其余字母小写

### 1.3、特殊情况

- **全大写或混合大小写**：统一处理后只保留首字母大写
- **多个连续辅音**：如 "chair" → "airchay"（"ch" 一起移动）
- **以 'y' 开头**：通常 'y' 被视为辅音，如 "yellow" → "ellowyay"

## 二、Returns

## 三、Python Solution(s)

## 四、JavaScript Solution(s)

