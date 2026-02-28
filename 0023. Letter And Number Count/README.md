# Letter and Number Count

Given a string, return a message with the count of how many letters and numbers it contains.

- Letters are `A-Z` and `a-z`.
- Numbers are `0-9`.
- Ignore all other characters.

Return `"The string has X letters and Y numbers."`, where `"X"` is the count of letters and `"Y"` is the count of numbers. If either count is 1, use the singular form for that item. E.g: `"1 letter"` instead of `"1 letters"` and `"1 number"` instead of `"1 numbers"`.

##  一、Returns

1. `countLettersAndNumbers("helloworld123")` should return `"The string has 10 letters and 3 numbers."`.
2. `countLettersAndNumbers("Catch 22")` should return `"The string has 5 letters and 2 numbers."`.
3. `countLettersAndNumbers("A1!")` should return `"The string has 1 letter and 1 number."`.
4. `countLettersAndNumbers("12345")` should return `"The string has 0 letters and 5 numbers."`.
5. `countLettersAndNumbers("password")` should return `"The string has 8 letters and 0 numbers."`.

## 二、解法、思路和坑

### 2.1、Python

1. 使用正则提取字符串中的字母和数字
   - 字母明确规定是`A-Za-z`，不用`w+`；
   - 数字是`0-9`，而不使用`\d+`
2. 使用`isalpha()`和`isdigit()`函数处理，但是`isalpha()`会匹配到`nǐ阿三hǎo`中的重音字符以及类似`é 你好 α`中的中文字符和西文字符也会被匹配到。
3. 严格按照只匹配英文字符的要求应该使用`string`库中的`ascii_letters`
4. 最后：
   - 尽量不用正则，降低空间复杂度
   - 遍历 + 计数
   - Unicode 字符是隐藏坑

### 2.2、JavaScript(s)

1. 只统计`A-Z` 和 `a-z`
1. 只统计 `0-9`
1. 忽略其他字符
1. 单复数处理

## 三、解法

### 3.1、Python Solution(s)

#### 3.1.1、使用str.isalpha()和str.isdigit()方法进行判定

```python
def count_letters_and_numbers_with_str_method(s):
    # 1. 判定是否是字符串
    if not isinstance(s, str):
        raise ValueError("输入的不是字符窜！")
    # 2. 判定字符串长度
    if len(s) == 0:
        raise ValueError("不能是空字符串！")

    # 3. 定义统计量
    letter_count = 0
    number_count = 0

    # 4. 开始遍历
    for char in s:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            number_count += 1

    letter_word = "letter" if letter_count == 1 else "letters"
    number_word = "number" if number_count == 1 else "numbers"

    return f"The string has {letter_count} {letter_word} and {number_count} {number_word}."
```

**隐藏坑**：中文字符和西文字符串以及重音字符都会被匹配。

#### 3.1.2、双sum写法

```python
import string
def count_letters_and_numbers_with_two_sums(s: str) -> str:
    # 1. 输入必须是非空字符串
    if not isinstance(s, str) or len(s) == 0:
        raise ValueError("输入必须是非空字符串！")

    # 2. 列表推导式进行统计
    letter_count = sum(c in string.ascii_letters for c in s)
    # string.ascii_letters只包含英文字母
    number_count = sum(c.isdigit() for c in s)

    return (f"The string has {letter_count} "
            f"{'letter' if letter_count == 1 else 'letters'} "
            f"and {number_count} "
            f"{'number' if number_count == 1 else 'numbers'}.")
print(count_letters_and_numbers_with_two_sums("helloworld123"))
```

#### 3.1.3、单次遍历 + 双计数（性能最优）

```python
def count_letters_and_numbers_with_for_and_two_counts(s: str) -> str:
    # 1. 输入必须是非空字符
    if not isinstance(s, str) or len(s) == 0:
        raise ValueError("输入必须是非空字符！")

    # 2. 双计数
    letter_count = number_count = 0

    # 3. 遍历
    for char in s:
        if char in string.ascii_letters:
            letter_count += 1
        elif char.isdigit():
            number_count += 1

    # 4. 返回
    return (
        f"The string has {letter_count} "
        f"{'letter' if letter_count == 1 else 'letters'} "
        f"and {number_count} "
        f"{'number' if number_count == 1 else 'numbers'}."
    )

print(count_letters_and_numbers_with_for_and_two_counts("helloworld123"))
```

### 3.2、JavaScript Solution(s)

#### 3.2.1、单次遍历 + charCode

“算法味”最浓的写法：

- 只遍历一次
- 不生成额外数组
- 精准控制 `ASCII` 范围
- 时间复杂度O(n)
- 空间复杂度O(1)

```js
function countLettersAndNumbers(str){
    // 1. 首先判定是否为字符串
    if(typeof str !== "string" || str.length === 0){
        throw new Error("Input must-be non-empty string!");
    }

    // 2. 计量统计
    let letterCount = 0;
    let numberCount = 0;

    // 3. 循环
    for(let i = 0; i < str.length; i++){
        const code = str.charCodeAt(i);
        // A-Z
        if(code >= 65 && code <= 90){
            letterCount++;
        }
        // a-z
        else if(code >= 97 && code <= 127){
            letterCount++;
        }
        // 0-9
        else if(code >= 48 && code <= 57){
            numberCount++;
        }
    }
    // 4. 定义字母大小写
    const letterWord = letterCount === 1 ? "letter" : "letters";
    const numberWord = numberCount === 1 ? "number" : "numbers";

    return `The string has ${letterCount} ${letterWord} and ${numberCount} ${numberWord}.`;
}
```

#### 3.2.2、使用正则

```js
function countLettersAndNumbersWithRepr(str){
    if(typeof str !== "string" || str.length === 0){
        throw new Error("Input must-be a non-empty string!");
    }

    // 2. 正则
    const letters = str.match(/[A-Za-z]/g) || [];
    const numbers = str.match(/[0-9]/g) || [];

    const letterCounts = letters.length;
    const numberCounts = numbers.length;

    return `The string has 
            ${letterCounts} ${letterCounts === 1 ? "letter" : "letters"} 
            and 
            ${numberCounts} ${numberCounts === 1 ? "number" : "numbers"}.`;
}
// console.log(countLettersAndNumbersWithRepr("123hellowo"));
```

#### 3.2.3、使用fliter()函数

```js
function countLettersAndNumbersWithFilter(str){
    // 1. 判定
    if(typeof str !== "string" || str.length === 0){
        throw new Error("输入必须是非空字符串！");
    }

    // 2. 解构赋值
    const chars = [...str];

    // 3. 利用filter计算字母
    const letterCounts = chars.filter(
        c =>
            (c >= "A" && c <= "Z") ||
            (c >="a" && c <= "z")).length;

    // 4. 利用filter计算数字
    const numberCounts = chars.filter(d => d >= "0" && d <= "9").length;
    return `The string has ${letterCounts} ${letterCounts === 1 ? "letter" : "letters"} and ${numberCounts} ${numberCounts === 1 ? "number" : "numbers"}.`;
}
// console.log(countLettersAndNumbersWithFilter('hellow1233'));
```

#### 3.2.4、使用reduce()函数

```js
function countLettersAndNumbersWithReduce(str){
    // 1. 判定
    if(typeof str !== "string" || str.length === 0){
        throw new Error("输入必须是非空字符窜！");
    }

    // 2. 解构
    const result = [...str].reduce((acc, cur) => {
        if((cur >= "A" && cur <= "Z") || (cur >= "a" && cur <= "z")){
            acc.letters++;
        } else if (cur >= "0" && cur <= "9"){
            acc.numbers++;
        }
        return acc;
    }, { letters:0, numbers: 0 })
    return `The string has ${result.letters} ${result.letters === 1 ? "letter" : "letters"} and ${result.numbers} ${result.numbers === 1 ? "number" : "numbers"}.`;
}
console.log(countLettersAndNumbersWithReduce("123hellowa1"));
```

