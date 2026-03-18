# Largest Number

Given a string of numbers separated by various punctuation, return the largest number.

- The given string will only contain numbers and separators.
- Separators can be commas (`","`), exclamation points (`"!"`), question marks (`"?"`), colons (`":"`), or semi-colons (`";"`).

##  一、题解和思路

### 1.1、题解

- 输入一个字符串，其中可能会存在各种各样的符号；但是只有小数点是合法的；
- 从字符串中提取数字（如果有包含小数点的也要提取）
- 返回最大的数字

### 1.2、思路

- 遍历字符串，如果遇到小数点，就应该拼接
- 使用正则提取数字（包含带小数点的）
- 使用max函数返回数组中最大的值；
- 返回最大值

## 二、Returns

- `largest_number("1,2")` should return `2`.
- `largest_number("4;15:60,26?52!0")` should return `60`.
- `largest_number("-402,-1032!-569:-947;-633?-800!-1012;-402,-723?-8102!-3011")` should return `-402`.
- `largest_number("12;-50,99.9,49.1!-10.1?88?16")` should return `99.9`.

## 三、Python Solution(s)

### 3.1、常规遍历解法

```python
def largest_number_normal_for(s: str) -> int or float:
    # 1. 判定用户输入
    if not isinstance(s, str):
        raise TypeError("Input must be a string!")

    # 2. 初始化统计
    nums = []
    current = ""

    # 3. 开始循环
    for i, ch in enumerate(s):
        # print(i, ch)
        # 因为是扫描字符串，所以要判定字符是否是数字跟小数点
        if ch.isdigit() or ch == ".":
            # 如果是数字且是小数点，我们就构建current
            current += ch  # 它会类似1 -> 5 -> :，现在还在构建的过程中，所以不能append
        elif ch == "-" and current == "":
            # 确定负数的情况，如果当前ch是-号，并且current为空，我们就构建负数
            current = "-"
        else:
            # if中的条件一定是要碰到数字跟小数点才会进行构建，else中我们要确定current是有值才能append
            if current and current != "-":
                nums.append(current)
                # 构建完后，将current重置
                current = ""
    # 4. 构建的时候如果最后一个字符不是特殊字符，那么current应该会有一个值存在
    if current and current != "-":
        nums.append(current)

    # 5. 求取最大值
    largest = max(nums, key=lambda x: float(x))

    # 6. 返回
    return float(largest) if "." in largest else int(largest)

largest_number_normal_for("4;15:60,26?52!0")
```

### 3.2、正则解法

```python
def largest_number_with_reg(s: str) -> int or float:
    import re
    # 1. pattern匹配正数、负数和小数
    pattern = re.compile(r"-?\d+\.?\d*")
    nums = re.findall(pattern, s)

    largest = max(nums, key=lambda x: float(x))
    return float(largest) if "." in largest else int(largest)
```

解释：

1. `re.findall(r"\d+\.?\d*", s)`会匹配：
   - `\d+`： 一个或多个数字
   - `\.?`：可选的小数点
   - `\d*`：小数点后可选的数字
2. 转成`float`，因为有可能是小数；
3. 用`max()`找出列表中最大值。

## 四、JavaScript Solution(s)

### 4.1、常规遍历

```js
function largestNumber(str){
    // 1、判定输入是否合法
    if(!typeof str === "string"){
        throw new TypeError("Input must be a string!");
    }

    // 2. 初始化
    let nums = [];
    let current = "";

    // 3. 开始循环
    for(const ch of str){
        // 判定是否为数字和是否为小数点
        // console.log(typeof ch); // string
        if(/\d/.test(ch) || ch === "."){
            // console.log(ch);
            current += ch;
            // console.log(current);
        } else if(ch === "-" && current === ""){
            current = "-";
        } else {
            if(current && current !== "-"){
                nums.push(current);
            }
            current = "";
        }
    }
    // 4. 处理最后一个值
    if(current){
        nums.push(current);
    }
    // console.log(nums);

    // 5. 求取最大值
    const largest = nums.reduce((max, cur) => {
        return parseFloat(cur) > max ? parseFloat(cur) : max;
    }, -Infinity);

    return largest % 1 === 1 ? parseInt(largest) : parseFloat(largest);
}
console.log(largestNumber("4;15:60,26?52!0"));
```

### 4.2、正则解法

```js
function largestNumberRegx(str){
    // pattern
    const matches = str.match(/-?\d+(\.\d+)?/g);
    if(!matches) {
        return null;
    }

    const largest = matches.reduce((max, val) => {
        return parseFloat(val) > max ? parseFloat(val) : max;
    }, -Infinity);

    // 返回整数还是浮点数
    return matches.includes(largest.toString()) && largest % 1 === 0 ? parseInt(largest) : largest;
}

console.log(largestNumberRegx("4;15:60,26?52!0"));
```

解释：

- 正则表达式跟python的有细小的差别
- `/-?\d+(\.\d+)?/g`
  - `/.../g`：正则字面量，`g` 表示全局匹配
  - `-?`：可选负号；
  - `\d+`：一个或多个数字；
  - `(\.\d+)?`：可选的小数部分（小括号分组）
  - `?`：0或者1个，表述小数部分可选；