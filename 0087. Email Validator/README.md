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

## 四、JavaScript Solution(s)

