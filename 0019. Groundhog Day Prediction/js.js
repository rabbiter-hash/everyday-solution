/* ==========================================
    第一种解法：常规解法，判定输入值是否为boolean
 ========================================== */

function groundhogDayPrediction(appearance){
    // 1. boolean判定
    if(typeof appearance === "boolean"){
        return appearance
            ? "Looks like we'll have six more weeks of winter."
            : "It's going to be an early spring.";
    }
    return "No prediction this year.";
}

/* ==========================================
    第二种解法：映射（数据驱动）
 ========================================== */
function groundhogDayPredictionMap(appearance) {
    const map = {
        true: "Looks like we'll have six more weeks of winter.",
        false: "It's going to be an early spring."
    };
    return typeof appearance === "boolean"
        ? map[appearance] : "No prediction this year.";
}

/* ==========================================
    第三种解法：includes判断型
 ========================================== */
function groundhogDogPredictionIncludes(appearance){
    if(![true, false].includes(appearance)){
        return "No prediction this year.";
    }
    return appearance
        ? "Looks like we'll have six more weeks of winter."
        : "It's going to be an early spring.";
}