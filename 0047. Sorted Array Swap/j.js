
function sortAndSwap(arr){
    // 1. 先排序数组
    const sortedArr = [...arr].sort((a, b) => a - b);

    // 2. 遍历原地交换
    for (let i = 0; i < sortedArr.length; i++){
        // console.log(i); // index: 0 - 11
        if(i % 3 === 0 && i > 0){
            // 将当前索引为i的值交换到它自己的前面
            // 注意这种交换写法，解构赋值，js最优雅的交换方法
            [sortedArr[i], sortedArr[i-1]] = [sortedArr[i-1], sortedArr[i]];
        }
    }
    console.log(sortedArr);
    return sortedArr;
}


sortAndSwap([12, 5, 8, 1, 3, 10, 2, 7, 6, 4, 9, 11]);