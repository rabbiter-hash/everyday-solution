# Bingo! Letter

Given a number, return the bingo letter associated with it (capitalized). Bingo numbers are grouped as follows:

| Letter | Number Range |
| :----: | :----------: |
| `"B"`  |     1-15     |
| `"I"`  |    16-30     |
| `"N"`  |    31-45     |
| `"G"`  |    46-60     |
| `"O"`  |    61-75     |

## 一、Python Solution（s）

### 1.1、常规解法

- 判定是否是数字以及数字的阈值

- 用`if...elif...else`

- 代码：

  ```python
  def get_bingo_letter(n):
      # 判定是否为数组
      if not isinstance(n, int) or n > 75:
          return "不是数字或者数字不符合要求！";
      
      if(1 <= n <= 15):
          return "B"
      elif(16 <= n <= 30):
          return "I"
      elif(31 <= n <= 45):
          return "N"
      elif(46 <= n <= 60):
          return "G"
      else:
          return "O"
  ```

### 1.2、数学差值法

- 判定是否是数字
- 判定是否在1-75之间
- 利用差值返回构造list，每个差15
  - B: 1-15
  - I: 16-30
  - N: 31-45
  - G: 46-60
  - O: 61-75

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/24 17:09
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: test.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_bingo_letters_with_list(n):
    # 1. 判定是否是数字
    if not isinstance(n, int) or n < 1 or n > 75:
        return "invalid"

    letters = ["B", "I", "N", "G", "O"]
    return letters[ int((n-1) / 15)]
    # return letters[ (n-1) // 15 ]

print(get_bingo_letters_with_list(20)) # I
print(get_bingo_letters_with_list(100)) # invalid
print(get_bingo_letters_with_list(75)) # 0
print(get_bingo_letters_with_list(50)) # G
```

### 1.3、map映射法

- 判定是否是数字
- 判定数字区间
- 构建map映射

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/24 17:09
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: test.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

def get_bingo_letters_with_map(n):
    # 1. 判定是否是数字
    if not isinstance(n, int) or n < 1 or n > 75:
        return "invalid"
    # 2. 构造映射
    mapping = {
        range(1, 16): "B", # 注意range左闭右开
        range(16, 31): "I",
        range(31, 46): "N",
        range(46, 61): "G",
        range(61, 76): "O",
    }
    
    # 3. 遍历
    for r, letter in mapping.items():
        if n in r:
            return letter
        
print(get_bingo_letters_with_map(15)) # B
print(get_bingo_letters_with_map(25)) # I
print(get_bingo_letters_with_map(35)) # N
print(get_bingo_letters_with_map(45)) # N
print(get_bingo_letters_with_map(55)) # G
print(get_bingo_letters_with_map(65)) # O
print(get_bingo_letters_with_map(75)) # O
print(get_bingo_letters_with_map(85)) # invalid
```

### 1.4、驱动映射

- 类似三，不过是先在全局构造好数据

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/24 17:09
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: test.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

BINGO_RULES = [
    (1, 15, "B"),
    (16, 30, "I"),
    (31, 45, "N"),
    (45, 60, "G"),
    (61, 75, "O"),
]
def get_bingo_letter_with_driver_mapping(n):
    # 1. 判定是否整数
    if not isinstance(n, int) or n < 1 or n > 75:
        return "invalid"

    # 2. 用n跟结构化数据去比较
    for start, end, letter in BINGO_RULES:
        if start <= n <= end:
            return letter
print(get_bingo_letter_with_driver_mapping(5)) # B
print(get_bingo_letter_with_driver_mapping(15)) # B
print(get_bingo_letter_with_driver_mapping(25)) # I
print(get_bingo_letter_with_driver_mapping(35)) # N
print(get_bingo_letter_with_driver_mapping(45)) # N
print(get_bingo_letter_with_driver_mapping(55)) # G
print(get_bingo_letter_with_driver_mapping(65)) # O
print(get_bingo_letter_with_driver_mapping(75)) # O
print(get_bingo_letter_with_driver_mapping(85)) # invalid

```



## 二、JavaScript Solution（s）

### 2.1、常规解法

- 判定输入的是否是数字

- 判定数字的阈值是否在`1-75`之间

- 用`if...else if...else`处理

- 代码：

  ```js
  function getBingoLettersNormal(n){
      if(!Number.isInteger || n < 1 || n > 75){
          return "invalid";
      }
  
      // 2. 开始判定
      if(n >=1 && n <= 15){
          return "B";
      } else if(n >= 16 && n <= 30) {
          return "I";
      } else if(n >= 31 && n <= 45) {
          return "N";
      } else if(n >=46 && n <= 60) {
          return "G";
      } else {
          return "O";
      }
  }
  
  console.log(getBingoLettersNormal(11));
  ```

- **注意**：JS **不支持数学里的区间链式比较**。

### 2.2、数学差值法

- 判定是否是数字
- 判定是否在1-75之间
- 利用差值返回构造list，每个差15
  - B: 1-15
  - I: 16-30
  - N: 31-45
  - G: 46-60
  - O: 61-75

```js
function getBingoLettersWithArray(n){
    // 1. 判定是否是数字
    if(!Number.isInteger(n) || n < 1 || n > 75){
        return "invalid";
    }

    // 2. 构建数组
    const letters = ["B", "I", "N", "G", "O"];

    // 3. 通过整除15获取返回值
    return letters[Math.floor((n-1) / 15)];
}

console.log(getBingoLettersWithArray(20)); // I
console.log(getBingoLettersWithArray(75)); // O
console.log(getBingoLettersWithArray(100)); // invalid
console.log(getBingoLettersWithArray(50)); // G

```

### 2.3、map映射

```js

function getBingoLettersWithMap(n){
    // 1. 判定是否是数字
    if(Number.isInteger(n) || n < 1 || n > 75){
        return "invalid"
    }
    const mapping = new Map([
        [[1, 15], "B"],
        [[16, 30], "I"],
        [[31, 45], "N"],
        [[46, 60], "G"],
        [[61, 75], "O"],
    ]);

    for(const [[start, end], letter] of mapping) {
        // console.log(start, end, letter);
        if( n >= start && n <= end) {
            return letter;
        }
    }
}

console.log(getBingoLettersWithMap('aaa')); // undefined
console.log(getBingoLettersWithMap('10')); // B
console.log(getBingoLettersWithMap('20')); // I
console.log(getBingoLettersWithMap('30')); // I
console.log(getBingoLettersWithMap('40')); // N
console.log(getBingoLettersWithMap('50')); // G
console.log(getBingoLettersWithMap('60')); // G
console.log(getBingoLettersWithMap('70')); // O
console.log(getBingoLettersWithMap('80')); // invalid
```

### 2.4、驱动映射数据

- 构造好驱动映射数据

```js

const BINGO_RULES = [
    [1, 15, "B"],
    [16, 30, "I"],
    [31, 45, "N"],
    [46, 60, "G"],
    [61, 75, "O"],
];

function getBingoLettersWithDriverData(n){
    // 1. 简单判定是否是数字
    if (typeof n !== "number") {
        return "Not a number!";
    }
    // 2. 遍历结构化数据并跟n进行比较
    for (const [start, end, letter] of BINGO_RULES) {
        if(n >= start && n <= end) {
            return letter;
        }
    }
}

console.log(getBingoLettersWithDriverData('aaa')); // Not a number
console.log(getBingoLettersWithDriverData('22')); // Not a number
console.log(getBingoLettersWithDriverData(11)); // B
console.log(getBingoLettersWithDriverData(21)); // I
console.log(getBingoLettersWithDriverData(31)); // N
console.log(getBingoLettersWithDriverData(41)); // N
console.log(getBingoLettersWithDriverData(51)); // G
console.log(getBingoLettersWithDriverData(61)); // O
console.log(getBingoLettersWithDriverData(81)); // undefined

```

