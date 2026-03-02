# Sum the Letters

Given a string, return the sum of its letters.

- Letters are A-Z in uppercase or lowercase
- Letter values are: `"A"` = 1, `"B"` = 2, ..., `"Z"` = 26
- Uppercase and lowercase letters have the same value.
- Ignore all non-letter characters.

## 一、Returns

1. `sum_letters("Hello")` should return `52`.
2. `sum_letters("freeCodeCamp")` should return `94`.
3. `sum_letters("The quick brown fox jumps over the lazy dog.")` should return `473`.
4. `sum_letters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci.")` should return `1681`.
5. `sum_letters("</404>")` should return `0`.

## 二、题解和思路

- 数据合法性检查
  - 检查输入是否是会字符串
  - 检查输入是否为空
- 映射A-Z，用mapping手动映射，也可以用`ord`函数
- 使用正则替换字符串中的特殊字符，题目要求只要字母，所以可以用`re.sub("[^a-zA-Z]", "", s)`，也就是非字母的都替换成`""`。
- 循环字符并增加到总和中；
- 返回值

## 三、Python Solution(s)

### 3.1、字典映射法

使用二的题解思路，采取映射方式求出结果。

```python
def sum_letters_with_chr(s):
    # 1. 判定是否符合要求
    if not isinstance(s, str) or len(s) == 0:
        return 0
    # 2. 映射
    mapping = {chr(i+97):i+1 for i in range(26)}
    print(mapping)

    # 3. 处理s中的特殊字符
    s = re.sub(r'[^a-zA-Z]', '', s)

    # 4. 开始循环
    total = 0
    for c in s.lower():
        if c in mapping:
            total += mapping[c]
    return total
print(sum_letters_with_chr('abc'))
```

优点：

- 直观，可处理大小写

缺点：

- 需手动维护字母映射
- 字典查找开销不小。

### 3.2、ord函数计算字母值

> ord("a") = 97; ord("A") = 65
>
> 字母值（小写）：ord(c.lower()) - ord("a") + 1；
>
> 遍历时只取`isalpha()`的值

```python
def sum_letters_with_ord(s):
    # 1. 判定是否为字符串
    if not isinstance(s, str) or len(s) == 0:
        raise ValueError('Empty string')
    if not s:
        return 0

    # 累加器
    total = 0

    # 2. 处理字符串中的特殊字符，因为只需要字母，可以用排除
    # s = re.sub(r'[^a-zA-Z]', '', s)

    # 3. 累加
    for char in s:
        if char.isalpha():
            total += ord(char.lower()) - ord('a') + 1

    # # 累加也可以换成一句话代码
    # total = sum(ord(c.lower()) - ord('a') + 1 for c in s)
    return total

print(sum_letters_with_ord("The quick brown fox jumps over the lazy dog."))
```

#### 3.2.1、优点

- 不需要字典，内存占用低；
- 可处理任意长度字符串

#### 3.2.2、缺点

循环写法稍长，如果想一步到位，需要生成器表达式。

### 3.3、生成器式一句代码

```python
def sum_letters_with_generator(s):
    return sum(ord(c.lower()) - ord('a') + 1 for c in s if c.islpah())
```

#### 3.3.1、优点

- 代码简洁
- Pythonic风格，效率较高
- 自动忽略非字母字符

#### 3.3.2、缺点

不是很直观。

##  四、JavaScript Solution(s)

### 4.1、for循环 + charCodeAt()

思路：

- 遍历字符串
- 判定是否为字母
- 用charCodeAt()计算值；

```js

/* ==========================================
    第一种解法：for 循环
 ========================================== */
function sumLettersWithFor(str){
    // 1. 判定数据是否和发
    if(typeof str !== "string") {
        throw new Error("输入必须是非空字符串！");
    }

    // 2. 累加器
    let total = 0;

    // 3. 循环
    for(let i = 0; i < str.length; i++){
        let char = str[i];

        // 正则提取字母
        if(/[a-zA-Z]/.test(char)) {
            total += char.toLowerCase().charCodeAt(0) - 96;
            // 97是'a'
        }
    }
    return total;
}

console.log(sumLettersWithFor("abc"));
console.log("a".charCodeAt(0));
```

### 4.2、用ASCII范围判断（更底层）

```js
function sumLettersWithAscii(str){
    // 1. 累加值
    let total = 0;

    for (let i=0; i < str.length; i++){
        let code = str[i].toLowerCase().charCodeAt(0);

        if(code >= 97 && code <= 122) {
            total += code - 96;
        }
    }
    return total;
}
console.log(sumLettersWithAscii("abc"));
```

### 4.3、split+reduce

```js
function sumLettersWithSplitPlusReduce(str){
    // 1. 判定输入的合法性
    if(typeof str !== "string" || str.length === 0){
        throw new Error("输入必须是非空字符串！");
    }

    // 2. 转小写 -> 分数组 -> 累加
    return str
        .toLowerCase()
        .split("")
        .reduce((acc, cur) => {
            let code = cur.charCodeAt(0);
            if(code >= 97 && code <= 122){
                return acc + (code - 96);
            }
            return acc;
        }, 0)
}
console.log(sumLettersWithSplitPlusReduce("abc"));
```

### 4.4、match + reduce

```js
function sumLettersWithMatchPlusReduce(str){
    // 1. 判定数据合法性
    if(typeof str !== "string" || str.length === 0) {
        throw new Error("输入必须是非空字符串！");
    }

    // 2. 将字母匹配出来
    const letters = str.match(/[a-zA-Z]/g);
    if(!letters) return 0;
    console.log(letters);
    return letters.reduce((acc, cur) => {
        return acc + cur.toLowerCase().charCodeAt(0) - 96;
    }, 0);

}
console.log(sumLettersWithMatchPlusReduce("ab c e"));
```

