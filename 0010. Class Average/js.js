
/* 注释 #=============================================
            *** 平均分计算
                scores：列表
                尽量用ES6解
      ============================================= # */

function getAverageGrade(scores){
    if(!Array.isArray(scores) || scores.length <= 1){
        console.log('必须是数组且数组长度要大于1');
        return;
    }
    const average = scores.reduce((sum, val) => sum+val, 0) / scores.length;

    const gradeMap = [
        [97, "A+"], [93, "A"], [90, "A-"],
        [87, "B+"], [83, "B"], [80, "B-"],
        [77, "C+"], [73, "C"], [70, "C-"],
        [67, "D+"], [63, "D"], [60, "D-"],
        [0, "F"]
    ];

    return gradeMap.find(([threshold]) => average >= threshold)[1];
}

function getAverageGradeByFor(scores){
    // 1. 判断输入
    if(!Array.isArray(scores) || scores.length <=1 ){
        alert('scores必须是数组且长度要大于1！');
        return;
    }

    // 2. 计算平均分
    const average = scores.reduce((sum, val)=> sum + val, 0) / scores.length;

    // 3. map
    const gradeMap = [
        [97, "A+"], [93, "A"], [90, "A-"],
        [87, "B+"], [83, "B"], [80, "B-"],
        [77, "C+"], [73, "C"], [70, "C-"],
        [67, "D+"], [63, "D"], [60, "D-"],
        [0, "F"]
    ];

    // 4. 使用for循环
    for (const [threshold, grade] of gradeMap){
        console.log(threshold);
        if(average >= threshold) {
            return grade;
        }
    }
}
getAverageGradeByFor([1, 2,3])