# String Math

Given a string with numbers and other characters, perform math on the numbers based on the count of non-digit characters between the numbers.

- If the count of characters separating two numbers is even, use addition.
- If it's odd, use subtraction.
- Consecutive digits form a single number.
- Operations are applied left to right.
- Ignore leading and trailing characters that aren't digits.

For example, given `"3ab10c8"`, return `5`. Add 3 and 10 to get 13 because there's an even number of characters between them. Then subtract 8 from 13 because there's an odd number of characters between the result and 8.

## 一、题解

根据两个数字之间的字符数量奇偶，决定**当前累计结果**与下一个数字的运算方式，并从左到右依次计算

## 二、思路

- 遍历字符串
- 拼数字
- 统计间隔
- 遇到新数字就结算
- 从左到右更新 result

## 三、Returns

1. `do_math("3ab10c8")` should return `5`.
2. `do_math("6MINUS4")` should return `2`.
3. `do_math("9plus3")` should return `12`.
4. `do_math("5fkwo#10i#%.<>15P=@20!#B/25")` should return `15`.
5. `do_math("a.67,1$lk6ldf34@#LD@]2d32d2'2l3,@l3L#@2gh35s09if=df#$t9sm49t0df3$^%[vc;:0:4mt")` should return `67`.

## 四、Python Solution(s)

```python
def do_math(s):
    import re
    # 1. 先取出所有数字
    nums = list(map(int, re.findall('\d+', s)))
    print(nums)

    # 2. 取出所有间隔
    gaps = re.split('\d+', s)
    print(gaps)

    # 3. 间隔长度
    gap_lengths = [len(gaps[i]) for i in range(1, len(gaps) - 1)]
    print(gap_lengths)

    # 4. 初始化result
    result = nums[0]

    # 5. 循环
    for i in range(1, len(nums)):
        if(gap_lengths[i - 1] % 2 == 0):
            result += nums[i]
        else:
            result -= nums[i]
    return result

do_math("3ab10c8")
```

## 五、JavaScript Solution(s)

```js
function doMath(str) {
    // 1. 提取数字数组和间隔数组
    const nums = str.match(/\d+/g).map(Number);
    console.log(nums);

    const gaps = str.split(/\d+/);
    console.log(gaps);

    // 2. 计算gaps的长度
    const gapLengths = [];
    for(let i = 1; i < gaps.length - 1; i++){
      gapLengths.push(gaps[i].length);
    }
    console.log(gapLengths);

    // 3. 初始化结果
    let result = nums[0];

    // 4. 循环读取
    for(let i = 1; i < nums.length; i++){
      if(gapLengths[i - 1] % 2 === 0){
        result += nums[i];
      } else {
        resutl -= nums[i];
      }
    }

    return result;
}


doMath("3ab10c8")
```

