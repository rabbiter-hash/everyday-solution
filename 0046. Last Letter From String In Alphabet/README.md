# Last Letter

Given a string, return the letter from the string that appears last in the alphabet.

- If two or more letters tie for the last in the alphabet, return the first one.
- Ignore all non-letter characters.

## 一、题解和思路

### 1.1、题解

输入一个字符串，得到的全是字母，然后返回在字母表顺序靠后的字母。比如`adezq`，返回`z`。如果有两个相同的字母，返回第一个。也就是可能要区分大小写。

### 1.2、思路

- 过滤出所有字母；用正则；
- 转小写；
- 用一个变量记录当前最大值
- 遍历更新最大值
- 返回结果

## 二、Returns

1. `get_last_letter("world")` should return `"w"`.
2. `get_last_letter("Hello World")` should return `"W"`.
3. `get_last_letter("The quick brown fox jumped over the lazy dog.")` should return `"z"`.
4. `get_last_letter("HeLl0")` should return `"L"`.
5. `get_last_letter("!#$ er@R asd fT.,> 2t0e9")` should return `"T"`.

## 三、Python Solution(s)

```python
def get_last_letter(s):
    import re
    # 1. 数据类型判定
    if not isinstance(s, str):
        raise TypeError('s must be a string')

    # 2. 提取字母
    letters = re.findall(r'[a-zA-Z]', s)

    if not letters:
        return ''

    # 3. 用小写取出字符串中最大的字符
    max_char = max(ch.lower() for ch in letters)

    # 3.遍历列表，找到第一个与最大字符串相等的字符
    for char in letters:
        if char.lower() == max_char:
            return char


print(get_last_letter("!#$ er@R asd fT.,> 2t0e9"))
```

## 四、JavaScript Solution(s)

```js

function getLastLetter(str){
    // 1. 通过正则取到字母列表
    const letters = str.match(/[a-zA-Z]/gi);

    // 2. 通过map转小写，并通过reduce累加取得最大值
    const maxChar = letters
        .map(ch => ch.toLowerCase())
        .reduce((a, b) => a > b ? a : b);

    // 3. 再次循环，使用小写对比
    for(let ch of letters){
        if(ch.toLowerCase() === maxChar){
            return ch;
        }
    }
}

getLastLetter("!#$ er@R asd fT.,> 2t0e9")
```

