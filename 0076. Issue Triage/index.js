function triageIssue(ms, message) {
    // 1. 将七天转换成毫秒数用于比较
    const sevenDaysMillSecs = 7 * 24 * 60 * 60 * 1000;
    // 2. 常量
    const BUMP = "bump";

    // 3. 开始比较
    if(ms < sevenDaysMillSecs) {
        return "leave it";
    } else if((ms >= sevenDaysMillSecs) && (message.toLowerCase().includes(BUMP))) {
        return "close it";
    } else {
        return "bump it";
    }
}

function triageIssueIf(ms, message) {
    // 1. 将七天转换成毫秒数用于比较
    const sevenDaysMillSecs = 7 * 24 * 60 * 60 * 1000;
    // 2. 常量
    const BUMP = "bump";

    // 3. 开始比较
    if(ms < sevenDaysMillSecs) {
        return "leave it";
    }

    if(ms >= sevenDaysMillSecs && message.toLowerCase().includes(BUMP)){
        return "close it";
    }

    return "bump it";
}

