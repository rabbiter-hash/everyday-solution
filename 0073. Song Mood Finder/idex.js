function getMood(genre, bpm){

    // 1. 建立映射表
    const moodMap = {
        "classical": [
            { low: 60, high: 109, mood: "focus" },
            { low: 110, high: 180, mood: "happy" }
        ],
        "electronic": [
            { low: 60, high: 89, mood: "focus" },
            { low: 90, high: 134, mood: "happy" },
            { low: 135, high: 180, mood: "hype" }
        ],
        "pop": [
            { low: 60, high: 180, mood: "happy" }
        ],
        "rock": [
            { low: 60, high: 129, mood: "happy" },
            { low: 130, high: 180, mood: "hype" }
        ]
    };

    // 2.判定是否在映射表汇总
    if(!moodMap[genre]){
        return null;
    }

    // 3. 遍历规则
    for(let rule of moodMap){
        // 开始判定
        if(bmp >= rule.low && bmp <= rule.high) {
            return rule.mood;
        }
    }

    return null
}