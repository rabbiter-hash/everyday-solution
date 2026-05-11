function getOldestPersonCompare(people){
    // 1. 定义一个空数组，用于存储结果
    let oldestNames = [];

    // 2. 定义一个最大年龄的变量，用于比较
    let maxAge = -Infinity;

    // 3. 开始循环
    for(let person of people){
        let name = person["name"];
        let age = person["age"];

        // 开始比较
        if(age > maxAge){
            // 如果年纪比最大年纪大，就要更新最大年纪的值
            maxAge = age;
            // 清空数组
            oldestNames = [name];
        } else if(age === maxAge){
            // 说明有同最大年龄的人，需要更新数组
            oldestNames.push(name);
        } else {
            console.log("不符合条件！");
        }
    }
    // 4. 返回数据
    return oldestNames;
}

console.log(getOldestPersonCompare(
    [{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]
))

function getOldestPersonIdiomatic(people){
    if (people.length === 0){
        return [];
    }

    // 2. 找到最大年龄
    const maxAge = Math.max(...people.map(person => person.age));
    console.log(maxAge);

    // 3. 筛选出所有年龄最大的人
    return people
        .filter(person => person.age === maxAge)
        .map(person => person.name);
}

console.log(getOldestPersonIdiomatic(
    [{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]
))