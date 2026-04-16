
function doMath(str){
    // 1. 利用正则取出数字列表和gaps
    const nums = str.match(/\d+/g).map(Number);
    const gaps = str.split(/\d+/);

    console.log(gaps);

    // 2. 获取gapsLength
    const gapsLengthArr = [];
    for(let i = 1; i < gaps.length - 1; i++){
        gapsLengthArr.push(gaps[i].length);
    }
    console.log(gapsLengthArr);
    // 3. 初始化结果
    let result = nums[0];

    // 4. 循环遍历
    for(let i = 1; i < nums.length; i++){
        if(gapsLengthArr[i-1] % 2 === 0){
            result += nums[i];
        } else {
            result -= nums[i];
        }
    }

    return result;
}

console.log(doMath("3ab10c8"));