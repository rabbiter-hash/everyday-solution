
function getBingoRange(letter){
    // 1. 结构化
    const mapping = {
        B: "1-15",
        I: "16-30",
        N: "31-45",
        G: "46-60",
        O: "61-75"
    };
    // 2. 解构赋值，取到区间的起始和结束位置
    const [start, end] = (mapping[letter].split("-"))
        .map(Number);

    // 3. 初始化结果存储
    const result = [];

    // 4. 循环
    for(let i = start; i <= end; i++){
        result.push(i);
    }

    return result;
}


function getBingRangeIdiomatic(letter){
    const [start, end] = {
            B: [1, 15],
            I: [16, 30],
            N: [31, 45],
            G: [46, 60],
            O: [61, 75]
          }[letter];

  return Array.from(
    { length: end - start + 1 },
    (_, i) => start + i
  );
}