# Lucky Number

Given a string of a person's first and last name, calculate their lucky number using the following rules:

- First and last names are separated by a space
- Find the vowel and consonant count for each name
- Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
- Do the same for the two larger counts and the larger name
- Subtract the smaller value from the larger one to get their lucky number

If the final value is zero (`0`), return `13`.

## 一、题解和思路

### 1.1、题解

输入一个以空格分开的人名，找到人名中所有的元音字母和辅音字母。

- 将最小的元音和最小的辅音进行相乘，再乘以名字中长度比较短的长度；
- 将最大的元音和最大的辅音进行相乘，再乘以名字中长度比较短的长度；
- 用大的值减去小的值获取到这个人的幸运数字。

### 1.2、思路

- 分别统计两个名字的元音数和辅音数
- 比较两个名字的长度，分出"较大名字"和"较小名字"
- 比较两个名字的元音数，取较小值和较大值
- 比较两个名字的辅音数，取较小值和较大值
- 计算：较小值 = 较小元音 × 较小辅音 × 较小名字长度
- 计算：较大值 = 较大元音 × 较大辅音 × 较大名字长度
- 幸运数字 = 较大值 - 较小值
- 如果结果为 0，返回 13

## 二、Returns

## 三、Python Solution(s)

```python
def get_lucky_number(name):
    # 1. 拆分姓名
    first, last = name.split()
    
    # 2. 定义元音字母（不区分大小写）
    vowels = 'aeiou'
    
    # 3. 统计元音和辅音数量的函数
    def count_vowels(word):
        return sum(1 for char in word.lower() if char in vowels)
    
    # 4. 统计每个名字的元音和辅音
    vowels_first = count_vowels(first)
    consonants_first = len(first) - vowels_first
    
    vowels_last = count_vowels(last)
    consonants_last = len(last) - vowels_last
    
    # 5. 确定较小/较大的名字长度
    smaller_name_len = min(len(first), len(last))
    larger_name_len = max(len(first), len(last))
    
    # 6. 确定较小/较大的元音数和辅音数
    smaller_vowels = min(vowels_first, vowels_last)
    larger_vowels = max(vowels_first, vowels_last)
    
    smaller_consonants = min(consonants_first, consonants_last)
    larger_consonants = max(consonants_first, consonants_last)
    
    # 7. 计算两个值
    smaller_value = smaller_vowels * smaller_consonants * smaller_name_len
    larger_value = larger_vowels * larger_consonants * larger_name_len
    
    # 8. 计算幸运数字
    result = larger_value - smaller_value
    
    # 9. 如果结果为0，返回13
    return 13 if result == 0 else result
```

## 四、JavaScript Solution(s)

```js
// 1. 拆分姓名
    const [first, last] = name.split(' ');
    
    // 2. 定义元音字母（不区分大小写）
    const vowels = 'aeiou';
    
    // 3. 统计元音数量的函数
    function countVowels(word) {
        let count = 0;
        for (let char of word.toLowerCase()) {
            if (vowels.includes(char)) {
                count++;
            }
        }
        return count;
    }
    
    // 4. 统计每个名字的元音和辅音
    const vowelsFirst = countVowels(first);
    const consonantsFirst = first.length - vowelsFirst;
    
    const vowelsLast = countVowels(last);
    const consonantsLast = last.length - vowelsLast;
    
    // 5. 确定较小/较大的名字长度
    const smallerNameLen = Math.min(first.length, last.length);
    const largerNameLen = Math.max(first.length, last.length);
    
    // 6. 确定较小/较大的元音数和辅音数
    const smallerVowels = Math.min(vowelsFirst, vowelsLast);
    const largerVowels = Math.max(vowelsFirst, vowelsLast);
    
    const smallerConsonants = Math.min(consonantsFirst, consonantsLast);
    const largerConsonants = Math.max(consonantsFirst, consonantsLast);
    
    // 7. 计算两个值
    const smallerValue = smallerVowels * smallerConsonants * smallerNameLen;
    const largerValue = largerVowels * largerConsonants * largerNameLen;
    
    // 8. 计算幸运数字
    const result = largerValue - smallerValue;
    
    // 9. 如果结果为0，返回13
    return result === 0 ? 13 : result;
```

