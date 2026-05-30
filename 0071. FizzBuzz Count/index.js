
function fizzBuzzCount(start, end){
    // 1. 初始化奇数
    let fCount = 0;
    let bCount = 0;

    // 2. 循环比那里
    for (let i = start; i <= end; i++) {
        if (i % 3 === 0) {
            console.log(i);
            fCount += 1;
        }
        if (i % 5 === 0) {
            console.log(i);
            bCount += 1;
        }
    }

    console.log(fCount, bCount);
    return {"fizz": fCount, "buzz": bCount}
}

function fizzBuzzCountIdiomatic(start, end){
    return Array.from({length: end - start + 1}, (_, idx) => start + idx)
        .reduce(
            (acc, i) => {
                if(i % 3 === 0) acc.fizz++;
                if(i % 5 === 0) acc.buzz++;
                return acc;
            },
            {fizz: 0, buzz: 0}
        );
}

fizzBuzzCountIdiomatic(1, 11);