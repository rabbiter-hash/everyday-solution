# Element Size

Given a window size, the width of an element in viewport width `"vw"` units, and the height of an element in viewport height `"vh"` units, determine the size of the element in pixels.

- The given window size and returned element size are strings in the format `"width x height"`, `"1200 x 800"` for example.
- `"vw"` units are the percent of window width. `"50vw"` for example, is 50% of the width of the window.
- `"vh"` units are the percent of window height. `"50vh"` for example, is 50% of the height of the window.

## 一、题解和思路

### 1.1、题解

- 如题

### 1.2、思路

- 数据合法性验证
  - 第一个参数`window_size`需要验证是否是合法的尺寸，可以用正则、数组拆分验证
  - 第二个参数 `element_vw`和 `element_vh` 用正则匹配数值以及`vw | vh`
- 定义`width`和`height`
- 返回`width` x `element_vw.strip("vw")` x `height X element_vh.strip("vh")`

## 二、Returns

- `get_element_size("1200 x 800", "50vw", "50vh")` should return `"600 x 400"`.
- `get_element_size("320 x 480", "25vw", "50vh")` should return `"80 x 240"`.
- `get_element_size("1000 x 500", "7vw", "3vh")` should return `"70 x 15"`.
- `get_element_size("1920 x 1080", "95vw", "100vh")` should return `"1824 x 1080"`.
- `get_element_size("1200 x 800", "0vw", "0vh")` should return `"0 x 0"`.
- `get_element_size("1440 x 900", "100vw", "114vh")` should return `"1440 x 1026"`.

## 三、Python Solution(s)

## 四、JavaScript Solution(s)

