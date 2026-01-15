
function arraySwapWithUnpacking(arr){
    if (arr.length !== 2) return
    // 解构赋值
    const [a, b] = arr;
    return [b, a];
}

function arraySwapWithExchange(arr) {
    // 原地交换
    [arr[0], arr[1]] = [arr[1], arr[0]];
    return arr;
}

function arraySwapWithIndex(arr){
    return [arr[1], arr[0]];
}

function arraySwapWithReverse(arr) {
    // 使用reverse()方法进行交换，会修改原数组
    return arr.reverse();
}
const aa = ['A', 'B'];
arraySwapWithReverse(aa);
console.log(aa);   // 原数组已经被修改

function arraySwapWithReverseNoChangeOriginalArray(arr) {
    // 不修改原数组进行转换
    return [...arr].reverse();
}

function arraySwapWithReverseAndSlice(arr) {
    // 同样不会改变原数组
    return arr.slice().reverse();
}

