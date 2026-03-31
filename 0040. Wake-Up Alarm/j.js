/* ==========================================
    第一种解法：循环遍历
 ========================================== */
function alarmCheck(alarmTime, wakeTime) {
    // 提取小时和分钟
    let alarmHour = parseInt(alarmTime.slice(0, 2));
    let alarmMinute = parseInt(alarmTime.slice(3, 5));

    let wakeHour = parseInt(wakeTime.slice(0, 2));
    let wakeMinute = parseInt(wakeTime.slice(3, 5));

    // 先比较小时
    if (wakeHour < alarmHour) {
        return "early";
    } else if (wakeHour === alarmHour) {
        // 同小时，比较分钟
        if (wakeMinute < alarmMinute) {
            return "early";
        } else if (wakeMinute <= alarmMinute + 10) {
            return "on time";
        } else {
            return "late";
        }
    } else {
        // wakeHour > alarmHour
        let minutesLate = (wakeHour - alarmHour) * 60 + (wakeMinute - alarmMinute);
        if (minutesLate <= 10) {
            return "on time";
        } else {
            return "late";
        }
    }
}