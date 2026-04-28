# Number Words

Given an integer from 0 to 99, return its English word representation.

- `0` returns `"zero"`.
- Numbers 1-19 have unique names (`"one"`, `"two"`, ..., `"ten"`, `"eleven"`, ..., `"eighteen"`, `"nineteen"`).
- Multiples of 10 from 20-90 have their own names (`"twenty"`, `"thirty"`, ..., `"eighty"`, `"ninety"`).
- Numbers 21-99 that are not multiples of 10 are written as two words joined by a hyphen. For example `"forty-two"` and `"fifty-three"`.

## 一、题解和思路

### 1.1、题解

根据输入数字的不同，输出相应数字的英文说法。

### 1.2、思路

- 首先编码 0 - 19 的英文说法，将输入的数字作为索引，进行返回；
- 编码整数数值
- 拼接其他数值

## 二、Returns

1. `get_number_words(0)` should return `"zero"`.
2. `get_number_words(10)` should return `"ten"`.
3. `get_number_words(19)` should return `"nineteen"`.
4. `get_number_words(30)` should return `"thirty"`.
5. `get_number_words(53)` should return `"fifty-three"`.
6. `get_number_words(7)` should return `"seven"`.
7. `get_number_words(12)` should return `"twelve"`.
8. `get_number_words(60)` should return `"sixty"`.
9. `get_number_words(67)` should return `"sixty-seven"`.
10. `get_number_words(98)` should return `"ninety-eight"`.

## 三、Python Solution(s)

### 3.1、常规分层编码

```python
def get_number_words(n):
    # 1. 首先编码20以下的
    words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    ]
    # print(len(words))  20

    # 2. 编码数字整数位
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty",
        "seventy", "eighty", "ninety"
    ]

    # 3. 判定输入的n
    if n < 20:
        return words[n]

    # 4. 判定是否整除
    ten = n // 10 # 整除获得十位数
    one = n % 10 # 取模取得个位数

    if one == 0:
        # 说明是整数
        return tens[ten]

    return tens[ten] + "-" + words[one]

print(get_number_words(21))
```

## 四、JavaScript Solution(s)

### 4.1、常规分层编码

```js

function getNumberWords(n){
    // 1. 编码20以下的数字
    const words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine", "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen"
    ];

    // 2. 编码整数，因为要从输入整除，所以0和10都要编码为空码
    const tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty",
        "seventy", "eighty", "ninety"
    ];

    // 3. 开始判定20以下的
    if(n < 20){
        // 直接以输入为索引进行提取
        return words[n];
    }

    // 4. 判定是否整除
    let ten = Math.floor(n / 10); // 十位数，需要用来作为提取十位数的索引
    let one = n % 10; // 个位数

    if(one === 0){
        // 说明是整数，就需要用到ten来提取数值
        return tens[ten];
    }

    return tens[ten] + "-" + words[one];
}
```

