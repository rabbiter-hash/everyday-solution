function sumOfDifferences(arr){
    // 1. 判定数据的合法性
    if(!Array.isArray(arr)){
        throw new Error("Arr is must an array!");
    }

    // 2. 初始化加和
    let total = 0;

    // 3. 循环比那里
    for(let i = 0; i < arr.length - 1; i++){
        console.log(i);
        total += arr[i+1] - arr[i];
    }

    console.log(total);
    return total;
}

sumOfDifferences([1, 3, 4]);


function sumOfDifferencesTelescopingMethod(arr){
    if(!Array.isArray(arr)){
        throw new Error("Arr must be an array!");
    }

    if(arr.length < 2){
        return 0;
    }

    return arr[arr.length - 1] - arr[0];
}