# Issue Triage



Given a number of milliseconds since the last post on an issue, and the last message posted on the issue, determine what you should do with the issue according to these rules:

- If the last message is less than 7 days ago, return `"leave it"`
- If the last message is 7 or more days ago and its content contains `"bump"` (case-insensitive), return `"close it"`
- Otherwise, return `"bump it"`

## 一、题解和思路

### 1.1、题解

根据参数一的毫秒数跟7天的毫秒数进行对比，返回三个分支的不同值。

### 1.2、思路

- 将七天的市场转成毫秒数（7 * 24 * 60 * 60 * 1000）
- 判断
  - 小于七天，返回"leave it"
  - 大于等于七天并且message含"bumps"，返回`close it`，注意`bump`是小写；
- 其他返回`bump it`

## 二、Returns

## 三、Python Solution(s)

### 3.1、if...else

```python
def triage_issue(ms, message):
    # 1. 七天的毫秒数
    seven_days_millsecs = 7 * 24 * 60 * 60 * 1000

    # 2. 开始判断
    if ms < seven_days_millsecs:
        # 如果 ms 小于七天，无条件返回 leave it
        return "leave it"
    elif ms >= seven_days_millsecs and "bump" in message.lower():
        return "close it"
    else:
        return "bump it"

```

### 3.2、单if

```python

def triage_issue_if(ms, message):
    # 用单if实现
    # 1. 七天的毫秒数
    seven_days_millsecs = 7 * 24 * 60 * 60 * 1000

    # 2. 判定
    if ms < seven_days_millsecs:
        return "leave it"

    if ms >= seven_days_millsecs and "bump" in message.lower():
        return "close it"

    return "bump it"
```

## 四、JavaScript Solution(s)

### 4.1、if...else

```js
function triageIssue(ms, message) {
    // 1. 将七天转换成毫秒数用于比较
    const sevenDaysMillSecs = 7 * 24 * 60 * 60 * 1000;
    // 2. 常量
    const BUMP = "bump";

    // 3. 开始比较
    if(ms < sevenDaysMillSecs) {
        return "leave it";
    } else if((ms >= sevenDaysMillSecs) && (message.toLowerCase().includes(BUMP))) {
        return "close it";
    } else {
        return "bump it";
    }
}
```

### 4.2、单if

```js
function triageIssueIf(ms, message) {
    // 1. 将七天转换成毫秒数用于比较
    const sevenDaysMillSecs = 7 * 24 * 60 * 60 * 1000;
    // 2. 常量
    const BUMP = "bump";

    // 3. 开始比较
    if(ms < sevenDaysMillSecs) {
        return "leave it";
    }

    if(ms >= sevenDaysMillSecs && message.toLowerCase().includes(BUMP)){
        return "close it";
    }

    return "bump it";
}

```

