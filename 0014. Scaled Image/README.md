# Scaled Image
Given a string representing the width and height of an image, and a number to scale the image, return the scaled width and height.

The input string is in the format "WxH". For example, "800x600".
The scale is a number to multiply the width and height by.
Return the scaled dimensions in the same "WxH" format.

## 一、Python Solution(s)

### 1.1、常规解法

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/26 13:44
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

from typing import Union
def scale_image(size: str, scale: Union[int, float]) -> str:
    # 如果是3.10后的版本应该是
    # def scale_image(size: str, scale: int | float) -> str:
    """ 注释 #=============================================
    		*** 传入图片的尺寸和scale，返回scale后的尺寸
    			- 1. size类似： "1200x720"
    			- 2. scale 可以是整数也可以是 浮点数
    			- 3. 如果是scale是2，需要返回 "2400x1440*
    	  ============================================= # """
    # 1. 判定是否有
    if not size or not scale:
        return
    # 2. 从字符串中提取宽和高的值
    width_str, height_str = size.split('x') # 注意：得到的是字符串

    # 3. 转数字
    width = int(width_str)
    height = int(height_str)

    # 4. 注意返回值，如果scale是小数的话，那么会得到浮点数，根据题目要求，都是整数，所以要加int
    return f"{int(width * scale)}x{int(height * scale)}"

print(scale_image('800x600', 2))

```

### 1.2、使用map转int

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/26 13:44
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

from typing import Union
from numbers import Real


def scale_image(size: str, scale: Real) -> str:

    # 如果是3.10后的版本应该是
    # def scale_image(size: str, scale: int | float) -> str:
    """ 注释 #=============================================
    		*** 传入图片的尺寸和scale，返回scale后的尺寸
    			- 1. size类似： "1200x720"
    			- 2. scale 可以是整数也可以是 浮点数
    			- 3. 如果是scale是2，需要返回 "2400x1440*
    			- 4. Real包含了int，float，Decimal，Fraction
    	  ============================================= # """
    # 1. 判定是否有
    if not size or not scale:
        return
    # 2. 使用map转换int
    width, height = map(int, size.lower().split('x')) # 可以接受大写的X

    # 3. 返回值
    return "{}x{}".format(int(width*scale), int(height*scale))

print(scale_image('800x600', 2))

```

### 1.3、列表推导式

```python
from numbers import Real
def scale_image(size: str, scale: Real) -> str:
    return "x".join(
        str(int(int(v) * scale))
        for v in size.split('x')
    )
```

### 1.4、正则表达式（格式校验+解析）

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/26 13:44
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

from typing import Union
from numbers import Real
import re

def scale_image(size: str, scale: Real) -> str:

    # 如果是3.10后的版本应该是
    # def scale_image(size: str, scale: int | float) -> str:
    """ 注释 #=============================================
    		*** 传入图片的尺寸和scale，返回scale后的尺寸
    			- 1. size类似： "1200x720"
    			- 2. scale 可以是整数也可以是 浮点数
    			- 3. 如果是scale是2，需要返回 "2400x1440*
    			- 4. Real包含了int，float，Decimal，Fraction
    	  ============================================= # """
    # 1. 正则规则
    pattern = r"(\d+)x(\d+)"
    match = re.fullmatch(pattern, size)
    print(match) # <re.Match object; span=(0, 7), match='800x600'>
    print(match.groups()) # ('800', '600')
    if not match:
        raise ValueError('Invalid size format!')

    # 2. 在match.groups()中提取数字
    width, height = map(int, match.groups())
    print(width, height, sep=" | ") # 800 | 600

    # 3. 返回
    return "{}x{}".format(int(width * scale), int(height * scale))

print(scale_image('800x600', 2))

```

### 1.5、map+lambda

```python
# -*- encoding: utf-8 -*- 
# @Time: 2026/1/26 13:44
# @Author: 、一叶孤城
# @Email: 28104511@qq.com
# @File: python.py
# @IDE: PyCharm
# @Motto: ABC(Always Be Coding)

from typing import Union
from numbers import Real
import re

def scale_image(size: str, scale: Real) -> str:

    # 如果是3.10后的版本应该是
    # def scale_image(size: str, scale: int | float) -> str:
    """ 注释 #=============================================
    		*** 传入图片的尺寸和scale，返回scale后的尺寸
    			- 1. size类似： "1200x720"
    			- 2. scale 可以是整数也可以是 浮点数
    			- 3. 如果是scale是2，需要返回 "2400x1440*
    			- 4. Real包含了int，float，Decimal，Fraction
    	  ============================================= # """
    # 1. lambda + map
    width, height = map(
        lambda x: int(int(x) * scale),
        size.split("x")
    )
    return f"{width}x{height}"

print(scale_image('800x600', 2))

```

###  1.6、一句话版本

```python
def scale_image(size, scale):
    # 一句话版
    return "x".join(
        str(int(int(_) * scale))
        for _ in size.split("x")
    )
```



### 1.#7、Python需要注意的点

- 字符 `*`  数字（整数），是重复字符串。比如：`"help * 2"="helphelp"`
- 数字 `*` 数字（整数），是整数。比如：`2 * 2 = 4`
- 数字 `*` 小数，得到的结果是`float`，比如` 2 * 1.5 = 3.0`

## 二、JavaScript Solution(s)

### 2.1、常规解法

```js
/* ==========================================
    第一种解法：常规解法，根据题目要求依次写代码
 ========================================== */
function scaleImage(size, scale){
    // 1. 数据判定
    if(typeof size !== "string" || typeof scale !== 'number'){
        throw new TypeError("Invalid input!");
    }

    // 2. 解构赋值，得到字符串
    const [width, height] = size.split('x').map(Number);
    console.log(width, height, typeof width, typeof height); // 1200 720 number number

    // 3. 直接返回
    return `${width * scale}x${height * scale}`;
}
console.log(300 * 1.5); // 450
console.log(scaleImage("1200x720", 1.5))
```

### 2.1、正则解法（校验解析）

```js
function scaleImageRe(size, scale) {
    console.log("第二种解法：==============================")
    // 1. 判定输入
    if(typeof size !== "string" || typeof scale !== "number"){
        throw new TypeError("Invalid input!");
    }

    // 2. 正则解析
    const pattern = /^(\d+)x(\d+)$/;
    const match = size.match(pattern);
    console.log("得到的正则匹配结果为：", match);
    if(!match) {
        throw new Error("Invalid size format!");
    }

    // 3. 解构赋值
    const [ , width, height] = match.map(Number);
    console.log(width, height, typeof width, typeof height);

    // 4. 返回
    return `${width * scale}x${height * scale}`;
}

console.log(scaleImageRe("1920x1080", 1.5))
```

### 2.3、replace + 回调

```js
function scaleImageReplace(size, scale) {
    console.log("第三种解法：==============================");
    // 1. 输入校验
    if(typeof size !== "string" || typeof scale !== "number") {
        throw new TypeErorr("Invalid input!");
    }

    // 2. 正则校验
    if(!/^(\d+)x(\d+)$/.test(size)){
        throw new Error("Invalid size format!");
    }

    // 3. 直接返回
    return size.replace(/\d+/g, n => Number(n) * scale);
}

console.log(scaleImageReplace("1270x720", 1.5));
```

### 2.4、函数式 map +join

```js
function scaleImageFunction(size, scale) {
    console.log("第四种解法：=============================");
    // 1. 数据输入判定
    if(typeof size !== "string" || typeof scale !== "number"){
        throw new TypeError("Invalid input!");
    }

    // 2. 求值
    const values = size.split("x").map(Number);
    console.log(values);

    // 3.判定size值是否合法
    if(values.length !== 2 || values.some(v => !Number.isInteger(v))){
        throw new Error("Invalid size format!");
    }

    // 4. 返回
    return values.map(v => v * scale).join("x");
}
console.log(scaleImageFunction("1920x1080", 1.5));
```



### 2.#1、JavaScrip需要注意的点

- Js可以隐式类型转换，也就是字符串`"1200"`在与数字进行数学运算的时候，它直接可以转成数字。
- 注意`脏`数据的清洗。