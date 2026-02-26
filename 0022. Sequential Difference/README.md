# Sequential Difference

Given an array of numbers, return a new array containing the value needed to get from each number to the next number.

- For the last number, use `0` since there is no next number.

For example, given `[1, 2, 4, 7]`, return `[1, 2, 3, 0]`.

**本质**：**相邻两个元素之间的差值（后一个减前一个）**。比较拗口的是：value needed to get from each number to the next number.



