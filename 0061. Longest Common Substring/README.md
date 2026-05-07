# Longest Common Substring

Given a string, return the longest substring that appears more than once.

- The substrings can overlap.

## 一、题解和思路

### 1.1、题解

从给定字符串中找出最长的子串。子串可以重叠。

### 1.2、思路

#### 1. 暴力枚举

- 枚举所有可能的子串
- 对每个子串检查它在原字符串中出现了不止一次；
- 记录最长的那个

#### 2、哈希 + 二分法

#### 3、后缀数组 + LCP

- 构建字符串的所有后缀

- 对所有后缀排序

- 相邻两个后缀的最长公共前缀（LCP）长度，就是某个子串在原始字符串中**至少出现两次**的长度

- 其中 LCP 的最大值就是答案的长度，然后再根据这个长度和出现的起始位置找到子串

- 如`banana`：

  | 起始索引 | 后缀字符串 | 排序后的后缀(升序) | 排序索引 | 相邻 LCP                  | LCP值                                                        |
  | -------- | :--------- | :----------------- | -------- | :------------------------ | ------------------------------------------------------------ |
  | 0        | banana     | a                  | 5        | —                         |                                                              |
  | 1        | anana      | ana                | 3        | LCP("a","ana") = 1        | LCP = 1（第一个字符 `'a'` 相同，第二个字符 `'a'` 的末尾 vs `'n'` → 不再相同） |
  | 2        | nana       | anana              | 1        | LCP("ana","anana") = 3    | LCP = 3（`"ana"` 完全出现在 `"anana"` 的前面）               |
  | 3        | ana        | banana             | 0        | LCP("anana","banana") = 0 | LCP = 0（首字符 `'a'` vs `'b'`）                             |
  | 4        | na         | na                 | 4        | LCP("banana","na") = 0    | LCP = 0（`'b'` vs `'n'`）                                    |
  | 5        | a          | nana               | 2        | LCP("na","nana") = 2      | LCP = 2（`"na"` 完全匹配 `"nana"` 的前两个字符）             |

最大 LCP = 3 → 子串 `"ana"`（来自 `"anana"` 和 `"ana"` 的前 3 个字符）。公共前缀长度 3 的字符串是 `"ana"`。

如何得到最长重复子串的原文

- 这对后缀是 `"ana"`（原索引 3）和 `"anana"`（原索引 1）。
- 取任意一个的前 3 个字符：就是 `"ana"`。

检查 `"ana"` 在原字符串中的位置：

- 索引 3 处有 `"ana"`（子串 `s[3:6]`）
- 索引 1 处也有 `"ana"`（`s[1:4]` 即 `"ana"`）

所以 `"ana"` 出现两次（索引 1 和 索引 3），且是最长的重复子串。

所以：

- **后缀数组（Suffix Array）**：按字典序排序后的所有后缀的原始起始索引列表。
- **LCP 数组（Longest Common Prefix）**：保存后缀数组中相邻两个后缀的公共前缀长度

重复子串问题 → 求 LCP 数组的最大值，如果最大值 > 0，就找到了最长的重复子串（可能出现多次，长度相同）；
如果最大值 = 0，说明没有重复非空子串。

## 二、Returns

1. `get_longest_substring("abracadabra")` should return `"abra"`.
2. `get_longest_substring("hello world hello")` should return `"hello"`.
3. `get_longest_substring("mississippi")` should return `"issi"`.
4. `get_longest_substring("ha ha ha ha ha ha ha")` should return `"ha ha ha ha ha ha"`.
5. `get_longest_substring("the quick brown fox jumped over the lazy dog that the quick brown fox jumped over")` should return `"the quick brown fox jumped over"`.

## 三、Python Solution(s)

### 3.1、暴力枚举

```python
def get_longest_substring(s):
    """
    暴力枚举法
        # 1、枚举所有可能的子串
        # 2、对每个子串检查它在原字符串中出现了不止一次。
        # 3、记录最长的那个
    """
    # 1. 首先获取字符串的长度
    s_length = len(s)
    print(s_length)

    # 2. 初始化最长子串
    longest_substring = ""

    # 3. 开始循环枚举
    for i in range(s_length):
        for j in range(i + 1, s_length + 1):
            substring = s[i:j]

            # 剪枝：如果当前子串长度 <= 已找到的最长长度，跳过
            if len(substring) <= len(longest_substring):
                continue

            # 检查这个子串是否在后面再次出现
            if substring in s[i+1:]:
                longest_substring = substring

    print(longest_substring)
    return longest_substring
get_longest_substring("abracadabra")
```

### 3.2、后缀数组 + LCP

## 四、JavaScript Solution(s)

### 4.2、暴力枚举

```js
function getLongestSubstring(str) {
    let longest = "";
    const countMap = new Map();

    // 统计所有子串出现次数
    for (let i = 0; i < str.length; i++) {
        for (let j = i + 1; j <= str.length; j++) {
            let sub = str.slice(i, j);
            countMap.set(sub, (countMap.get(sub) || 0) + 1);
        }
    }

    // 找出现次数大于 1 的最长子串
    for (let [sub, count] of countMap) {
        if (count > 1 && sub.length > longest.length) {
            longest = sub;
        }
    }

    return longest;
}

// getLongestSubstring("abracadabra");
let str = "abracadabra";
let sub = "abra";
console.log(str.split(sub)); // [ '', 'cad', '' ]
console.log(str.split(sub).length - 1); // 2

let a = "aaa";
let suba = "a";
console.log(a.split(suba)); // [ '', '', '', '' ]
console.log(a.length); // 3
console.log(a.split(suba).length); // 4
```

### 4.2、后缀数组 + LCP