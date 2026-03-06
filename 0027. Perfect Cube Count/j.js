/* ==========================================
    第一种解法：整数枚举法
 ========================================== */
function countPerfectCubes(a, b) {
  // 1. 确定区间的最小值和最大值
  const low = Math.min(a, b);
  const high = Math.max(a, b);

  // 2. 从 n=0 开始，找到区间内第一个立方数 n³ >= low
  let n = 0;

  // 2a. 如果 low < 0，需要向负方向移动 n，直到 n³ <= low
  while (n ** 3 > low) {
    n -= 1;
  }

  // 2b. 调整 n，保证 n³ >= low
  while (n ** 3 < low) {
    n += 1;
  }

  // 3. 初始化计数器
  let count = 0;

  // 4. 从左边界 n 开始枚举，每次 n³ <= high 就计数
  while (n ** 3 <= high) {
    count += 1; // 统计一个完美立方数
    n += 1;     // 移动到下一个整数
  }

  // 5. 返回区间内完美立方数总数
  return count;
}

// 测试
console.log(countPerfectCubes(-64, 64)); // 输出 9
console.log(countPerfectCubes(0, 27));   // 输出 4 (0,1,8,27)
console.log(countPerfectCubes(-27, -1)); // 输出 3 (-27,-8,-1)