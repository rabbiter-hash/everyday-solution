# Email Validator

Given a string, determine if it is a valid email address using the following constraints:

- It must contain exactly one `@` symbol.
- The local part (before the `@`):
  - Can only contain letters (`a-z`, `A-Z`), digits (`0-9`), dots (`.`), underscores (`_`), or hyphens (`-`).
  - Cannot start or end with a dot.
- The domain part (after the `@`):
  - Must contain at least one dot.
  - Must end with a dot followed by at least two letters.
- Neither the local or domain part can have two dots in a row.

## 一、题解和思路

### 1.1、题解

合法邮箱验证。

### 1.2、思路

硬性条件：字符串中必须包含`@`，且只能有一个。

分成两个部分检查：

### 1.2.1、Localpart

通过`@`分割的`Localpart`必须满足：

1. 不能为空；
2. 不能以`.`开头和结尾；
3. 不能有两个连续的`.`；
4. 只能包含允许的字符
   - 英文字母 `a-z`、`A-Z`
   - 数字 `0-9`
   - 点 `.`
   - 下划线 `_`
   - 连字符 `-`

### 1.2.2、DomainPart

1. 必须包含点，不能有连续两个点
2. 必须以点加至少两个英文字母结尾

## 二、Returns

1. `validate("a@b.cd")` should return `True`.
2. `validate("hell.-w.rld@example.com")` should return `True`.
3. `validate(".b@sh.rc")` should return `False`.
4. `validate("example@test.c0")` should return `False`.
5. `validate("freecodecamp.org")` should return `False`.
6. `validate("develop.ment_user@c0D!NG.R.CKS")` should return `True`.
7. `validate("hello.@wo.rld")` should return `False`.
8. `validate("hello@world..com")` should return `False`.
9. `validate("develop..ment_user@c0D!NG.R.CKS")` should return `False`.
10. `validate("git@commit@push.io")` should return `False`.

## 三、Python Solution(s)

### 3.1、Fundamental algorithm

```python
def validate(email):
    # 1. 判定@在email中的数量，要有且只有一个
    if(email.count('@') != 1):
        return False
    # 2. 通过@进行分割字符串
    local_part, domain_part = email.split('@')
    # 2.1、如果local_part或者domain_part为空，就返回False
    if(not local_part or not domain_part):
        return False
    # 3. 对local_part进行判定
    ## 3.1、local_part不能以.开始或者结束
    if(local_part.startswith('.')):
        return False
    if(local_part[-1] == '.'):
        return False
    ## 3.2、local_part不能连续出现两个..
    # 不能包含连续的..
    if ('..' in local_part):
        return False
    ## 3.3、local_part必须包含题目要求的字符
    for char in local_part:
        is_letter = char.isalpha()
        is_digit = char.isdigit()
        is_symbol = char in ['-', '_', '.']
        if(not is_letter and not is_digit and not is_symbol):
            return False
    # 4. 对domain_part进行判定
    ## 4.1、题目要求domain_part需要一个.，但是不能有两个连续的
    if('.' not in domain_part or '..' in domain_part):
        return False
    ## 4.2、找到最后一个.并进行分割
    dot_split_suffix = domain_part.split('.')[-1]
    ## 4.3、后缀的长度不能低于2
    if(len(dot_split_suffix) < 2):
        return False
    ## 4.4、后缀必须是字母
    for char in dot_split_suffix:
        if(not char.isalpha()):
            return False
    return True

validate("hell.-w.rld@example.com")
```

## 四、JavaScript Solution(s)

### 4.1、Fundamental algorithm

```js
function validate(email) {
    // 1. 检查是否包含@，没有就return false
    let atIndex = email.indexOf("@");
    console.log(atIndex);
    console.log(email.lastIndexOf("@"));
    // 判定@的数量和位置
    if((atIndex === -1) || atIndex !== email.lastIndexOf("@")) {
        return false;
    }
    // 2. 通过@拆分成localpart和domain part
    let localPart = email.slice(0, atIndex);
    let domainPart = email.slice(atIndex + 1, );
    console.log(localPart);
    console.log(domainPart);

    // 如果local和domain都为空，肯定不是正确的
    if((localPart === '') || (domainPart === '')) {
        return false;
    }
    // 3. 检查localpart部分
    // 3.1、检查localPart的点的位置
    if((localPart.startsWith('.')) || localPart.endsWith('.')) {
        return false;
    }
    // 3.2、判定是否有连续的..
    if(localPart.includes('..')) {
        return false;
    }
    // 3.3、检查local的每个字符
    for(let i = 0; i < localPart.length; i++){
        let char = localPart[i];
        // console.log(char);
        let isLetter = (
            (char >= 'a' && char <= 'z') ||
            (char >= 'A' && char <= 'Z')
        );
        let isDigit = (
            char >= '0' && char <= '9'
        );
        let isSymbol = (
            char === '.' ||
            char === '-' ||
            char === '_'
        );

        // 循环的每个字符都应该满足上面三个条件
        if(!isLetter && !isDigit && !isSymbol) {
            return false;
        }
    }
    // 4. 检查domain part部分
    // 4.1、domain part必须包含点，且不能有连续的点
    // console.log(domainPart.includes('.'));
    // console.log(domainPart.includes('..'));
    if(!domainPart.includes('.') || domainPart.includes('..')) {
        // 如果不不包含点或者包含两个点，直接false
        return false;
    }
    // 4.2、检查最后一个点后最少包含两个英文字母
    // 记得这里一定要用lastIndexOf
    let dotIndex = domainPart.lastIndexOf('.');
    let suffix = domainPart.slice(dotIndex + 1);

    // 4.3、如果点后的长度小于2，直接false
    if(suffix.length < 2) {
        return false;
    }

    //4.4、最后的两个字符必须是英文字母
    for(let i = 0; i < suffix.length; i++) {
        // 提取出字符
        let char = suffix[i];
        // 字母表达式
        let isLetter =
            (char >= 'a' && char <= 'z') ||
            (char >= 'A' && char <= 'Z');

        if (!isLetter) {
            return false;
        }
    }
    return true;
}

validate('john.doe_123@example.com'); // true
validate('.john@example.com');        // false
validate('john..doe@example.com');    // false
validate('john@example.c');           // false
validate('john@example..com');        // false
validate('john@example.com.cn');      // true

console.log("a".indexOf("bbb"))

console.log("bbbbcceafeadff".lastIndexOf("f"))
```

